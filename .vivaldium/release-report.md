# Vivaldi 1.2.490 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `51.0.2704.79` at `0a967bea2f0b592106657f0af87985ec6b6fe44d`.
* Published archive SHA-256: `1bc54a2162dcfa5f08c81fd3dd7972b309aded80afce979ab69741eff14098b3`.
* Complete normalized fingerprint: `947f1f93df435b535e42f1cca9f3b274640b949d315009b85c1f5fd2d7f5108c`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.2, announced 2016-06-02): Ready to make your own mouse gestures? Now you can with Vivaldi 1.2
Official announcement synopsis: Mouse gestures have been a popular feature of the Vivaldi browser since we launched our first TP last year. With version 1.2 we’re letting you make your
Source: https://vivaldi.com/blog/vivaldi-1-2-with-mouse-gestures/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
2035 changed paths in 4 patch files (7618330 patch bytes).

Paths: DEPS, build/branding_value.sh, build/chrome_settings.gypi, build/common.gypi, build/git-hooks/pre-commit, build/gyp_chromium.py, build/install-build-deps.sh, build/json_schema_bundle_compile.gypi, build/json_schema_bundle_registration_compile.gypi, build/json_schema_compile.gypi, build/mac/copy_framework_unversioned.sh, build/mac/tweak_info_plist.py and 2023 more.

## browser
1279 changed paths in 3 patch files (36816798 patch bytes).

Paths: chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe.vsprops, chrome/app/chrome_exe_main_mac.c, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version, chrome/app/version_assembly/chrome_exe_manifest.template, chrome/app/version_assembly/chrome_exe_manifest_action.gypi, chrome/app/version_assembly/version_assembly_manifest.template and 1267 more.

## extensions
73 changed paths in 1 patch files (144910 patch bytes).

Paths: extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/storage/storage_frontend.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/app_window/app_web_contents_helper.cc, extensions/browser/app_window/app_window.cc, extensions/browser/app_window/app_window.h, extensions/browser/extension_event_histogram_value.h, extensions/browser/extension_function.cc, extensions/browser/extension_function_histogram_value.h and 61 more.

## components
112 changed paths in 1 patch files (180828 patch bytes).

Paths: components/autofill/core/browser/personal_data_manager.cc, components/bookmarks.gypi, components/bookmarks/browser/bookmark_codec.cc, components/bookmarks/browser/bookmark_codec.h, components/bookmarks/browser/bookmark_codec_unittest.cc, components/bookmarks/browser/bookmark_index.cc, components/bookmarks/browser/bookmark_match.cc, components/bookmarks/browser/bookmark_match.h, components/bookmarks/browser/bookmark_model.cc, components/bookmarks/browser/bookmark_model.h, components/bookmarks/browser/bookmark_model_unittest.cc, components/bookmarks/browser/bookmark_node.cc and 100 more.

## rendering
131106 changed paths in 257 patch files (835978423 patch bytes).

Paths: content/app/strings/content_strings.gyp, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/download/base_file.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc, content/browser/download/download_resource_handler.h and 131094 more.

## ui
26 changed paths in 1 patch files (26920 patch bytes).

Paths: ash/ash_strings.gyp, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/l10n/l10n_util.cc, ui/base/resource/resource_bundle.cc, ui/base/resource/resource_bundle_android.cc, ui/base/resource/resource_bundle_ios.mm, ui/base/resource/resource_bundle_mac.mm, ui/base/ui_base_tests_bundle.gypi, ui/resources/ui_resources.gyp, ui/shell_dialogs/select_file_dialog_win.cc, ui/strings/ui_strings.gyp and 14 more.

## networking
3 changed paths in 1 patch files (1969 patch bytes).

Paths: net/base/url_util.h, net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc.

## media
122 changed paths in 1 patch files (1094208 patch bytes).

Paths: gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/gles2_conform_support/gles2_conform_support.gyp, gpu/gpu.gyp, gpu/ipc/service/gpu_channel.cc, gpu/ipc/service/gpu_channel.h, gpu/ipc/service/gpu_channel_manager.h, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h, media/base/container_names.cc, media/base/container_names.h, media/base/container_names_unittest.cc and 110 more.

## dependencies
63624 changed paths in 177 patch files (1584717553 patch bytes).

Paths: third_party/angle/.clang-format, third_party/angle/.gitattributes, third_party/angle/.gitignore, third_party/angle/AUTHORS, third_party/angle/BUILD.gn, third_party/angle/CONTRIBUTORS, third_party/angle/DEPS, third_party/angle/LICENSE, third_party/angle/README.chromium, third_party/angle/README.md, third_party/angle/angle.isolate, third_party/angle/angle_on_all_platforms.isolate and 63612 more.

## other
4041 changed paths in 8 patch files (57780258 patch bytes).

Paths: .gitattributes, .gitmodules, apps/app_load_service.cc, apps/launcher.cc, base/allocator/BUILD.gn, base/allocator/allocator.gyp, base/allocator/allocator_check.cc, base/allocator/allocator_shim_win.cc, base/allocator/allocator_shim_win.h, base/allocator/prep_libc.py, base/base.gyp, base/base.gypi and 4029 more.
