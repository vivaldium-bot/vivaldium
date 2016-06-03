#!/usr/bin/env python3
"""Snapshot concise, attributed summaries from official Vivaldi release posts.

This reads the user-supplied changelog inventory and stores only a short,
machine-extracted synopsis with its source URL and content digest. It does not
use a language model and it never treats an announcement as original Git
history.
"""
from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import time
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / 'config/changelogs.json'
OUTPUT = ROOT / 'config/release-notes.json'
UA = 'vivaldium-rebuild/7 (+https://github.com/vivaldium-bot/vivaldium)'


class ArticleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.description = ''
        self.article_depth = 0
        self.paragraph_depth = 0
        self.paragraphs: list[str] = []
        self.current: list[str] = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'meta' and attrs.get('name', '').lower() == 'description':
            self.description = attrs.get('content', '').strip()
        if tag == 'article':
            self.article_depth += 1
        if tag == 'p' and self.article_depth:
            self.paragraph_depth += 1

    def handle_data(self, data):
        if self.paragraph_depth:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag == 'p' and self.paragraph_depth:
            self.paragraph_depth -= 1
            text = ' '.join(''.join(self.current).split())
            self.current = []
            if text:
                self.paragraphs.append(text)
        if tag == 'article' and self.article_depth:
            self.article_depth -= 1


def synopsis(html: bytes) -> str:
    parser = ArticleText()
    parser.feed(html.decode('utf-8', 'replace'))
    # Preserve only a short factual excerpt. This is a release context field,
    # not a generated interpretation or an attribution to individual patches.
    candidates = [parser.description, *parser.paragraphs]
    for value in candidates:
        value = re.sub(r'\s+', ' ', value).strip()
        if len(value) >= 50:
            return value[:600].rsplit(' ', 1)[0] + ('…' if len(value) > 600 else '')
    return parser.description or 'Official announcement did not expose a usable synopsis.'


def fetch(url: str) -> tuple[str, str]:
    response = urlopen(Request(url, headers={'User-Agent': UA, 'Accept': 'text/html'}), timeout=60)
    with response:
        body = response.read()
    return synopsis(body), hashlib.sha256(body).hexdigest()


def literal_env(name: str) -> str | None:
    """Read one literal secret; never source or execute .env."""
    if os.environ.get(name):
        return os.environ[name]
    dot_env = ROOT / '.env'
    if not dot_env.is_file():
        return None
    for line in dot_env.read_text().splitlines():
        line = line.strip()
        if line.startswith('export '):
            line = line[7:].lstrip()
        key, separator, value = line.partition('=')
        if separator and key.strip() == name:
            value = value.strip()
            if value[:1] in ('"', "'"):
                if len(value) < 2 or value[-1] != value[0]:
                    raise RuntimeError(f'{name} has an unterminated quote')
                value = value[1:-1]
            if not value or any(char.isspace() for char in value):
                raise RuntimeError(f'{name} must be a literal token value')
            return value
    return None


def request_json(url: str, token: str, payload: dict | None = None) -> dict:
    body = json.dumps(payload).encode() if payload else None
    request = Request(url, data=body, headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'HTTP-Referer': 'https://github.com/vivaldium-bot/vivaldium',
        'X-Title': 'Vivaldium release-note context',
        'User-Agent': UA,
    })
    with urlopen(request, timeout=90) as response:
        return json.loads(response.read())


def free_model(token: str) -> str:
    models = request_json('https://openrouter.ai/api/v1/models', token)['data']
    candidates = [item['id'] for item in models if item.get('id', '').endswith(':free')]
    if not candidates:
        raise RuntimeError('OpenRouter returned no free models')
    # Stable preference order keeps reruns explainable when several free models
    # are offered. The fallback remains an explicitly free model from the API.
    preferred = (
        'google/gemma-4-31b-it:free',
        'google/gemma-4-26b-a4b-it:free',
        'qwen/qwen3.8-27b:free',
        'liquid/lfm-2.5-2.6b:free',
    )
    return next((model for model in preferred if model in candidates), sorted(candidates)[0])


def model_summary(token: str, model: str, note: dict) -> str:
    source = note['synopsis']
    prompt = (
        'Write one factual release-context paragraph of at most 70 words from '
        'this official Vivaldi announcement excerpt. Preserve named features and '
        'versions when stated. Do not invent details. Do not mention Git, patches, '
        'code, authors, or attribution. Return only the paragraph.\n\n'
        f'Release: Vivaldi {note["tag"]}\nDate: {note["published"]}\n'
        f'Announcement title: {note["title"]}\nExcerpt: {source}'
    )
    payload = {
        'model': model,
        'temperature': 0,
        'max_tokens': 130,
        'messages': [
            {'role': 'system', 'content': 'You produce concise, source-grounded release summaries.'},
            {'role': 'user', 'content': prompt},
        ],
    }
    response = request_json('https://openrouter.ai/api/v1/chat/completions', token, payload)
    raw = response['choices'][0]['message'].get('content')
    if not isinstance(raw, str):
        raise RuntimeError('OpenRouter returned no final text for ' + note['tag'])
    text = raw.strip()
    text = re.sub(r'\s+', ' ', text).strip(' "')
    if not text or len(text.split()) > 70:
        raise RuntimeError(f'OpenRouter returned an invalid summary for {note["tag"]}')
    return text


def write_snapshot(document: dict) -> None:
    temporary = OUTPUT.with_suffix('.tmp')
    temporary.write_text(json.dumps(document, indent=2, sort_keys=True, ensure_ascii=False) + '\n')
    temporary.replace(OUTPUT)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sleep', type=float, default=0.35)
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--openrouter', action='store_true', help='add free-model release-context summaries')
    parser.add_argument('--tag', help='summarize only one release family, such as 1.2')
    parser.add_argument('--limit', type=int, default=0, help='maximum new model requests; zero means all')
    args = parser.parse_args()
    inventory = json.loads(INVENTORY.read_text())
    old = json.loads(OUTPUT.read_text()) if OUTPUT.exists() and not args.force else {'notes': []}
    cached = {row['source']: row for row in old.get('notes', [])}
    notes = []
    for entry in inventory['entries']:
        source = entry['source']
        if source in cached:
            notes.append(cached[source])
            continue
        text, digest = fetch(source)
        notes.append({
            'tag': entry['tag'],
            'published': entry['date'],
            'title': entry['title'],
            'source': source,
            'synopsis': text,
            'source_html_sha256': digest,
            'attribution': 'Vivaldi Technologies official release announcement',
        })
        print('fetched', entry['tag'], flush=True)
        time.sleep(args.sleep)
    document = {
        'format': 1,
        'inventory_sha256': inventory['manifest_sha256'],
        'method': 'Short source excerpt extracted from official announcement HTML; no model-generated text.',
        'limitation': 'Release-level context only. It does not reconstruct original commits or assign features to synthetic subsystem commits.',
        'notes': sorted(notes, key=lambda row: (row['published'], row['tag'], row['source'])),
    }
    if args.openrouter:
        token = literal_env('OPENROUTER_KEY')
        if not token:
            raise RuntimeError('OPENROUTER_KEY is required for --openrouter')
        model = free_model(token)
        previous = {row['source']: row for row in old.get('notes', [])}
        attempts = 0
        for note in document['notes']:
            if args.tag and note['tag'] != args.tag:
                continue
            cached_note = previous.get(note['source'], {})
            cached = cached_note.get('openrouter')
            if cached and cached.get('summary') and cached.get('model') == model and cached.get('source_html_sha256') == note['source_html_sha256']:
                note['openrouter'] = cached
                continue
            if args.limit and attempts >= args.limit:
                break
            attempts += 1
            try:
                summary = model_summary(token, model, note)
            except HTTPError as error:
                if error.code != 429:
                    raise
                note['openrouter'] = {
                    'model': model,
                    'prompt_format': 1,
                    'source_html_sha256': note['source_html_sha256'],
                    'status': 'rate-limited',
                }
                print('rate-limited', note['tag'], 'with', model, flush=True)
                write_snapshot(document)
                break
            note['openrouter'] = {
                'model': model,
                'prompt_format': 1,
                'source_html_sha256': note['source_html_sha256'],
                'summary': summary,
            }
            print('summarized', note['tag'], 'with', model, flush=True)
            # Preserve completed model work across free-tier rate limits.
            write_snapshot(document)
            time.sleep(args.sleep)
        document['openrouter'] = {
            'enabled': True,
            'model': model,
            'method': 'Free OpenRouter model, temperature 0, with official announcement excerpt only. Rate limits are accepted without retrying.',
        }
    write_snapshot(document)
    print(f'wrote {len(notes)} release-note summaries to {OUTPUT}')


if __name__ == '__main__':
    main()
