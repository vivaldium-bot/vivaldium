# Vivaldi 1.5.658 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `54.0.2840.100` at `371dfa8590ab628cae87fdc86cb7e8e0b1dbadd4`.
* Published archive SHA-256: `37c1a149066b9ece402e081736daa48fbc9ae485a8ffff17d6cd45bf7684fc51`.
* Complete normalized fingerprint: `2dfcfdef58f5b29c76f62a063b7f7a45b5d2fcc628e58998f07ac45f191bc2b7`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.5, announced 2016-11-22): Lighten up your Day with Vivaldi Browser
Official announcement synopsis: The latest version of Vivaldi includes a number of new features that we can’t wait for you to
Source: https://vivaldi.com/blog/lighten-up-your-day-with-vivaldi-browser-2/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
2150 changed paths in 5 patch files (7973422 patch bytes).

Paths: BUILD.gn, DEPS, build/branding_value.sh, build/chrome_settings.gypi, build/common.gypi, build/config/BUILD.gn, build/config/BUILDCONFIG.gn, build/config/chrome_build.gni, build/config/compiler/BUILD.gn, build/config/features.gni, build/config/gcc/BUILD.gn, build/config/mac/mac_sdk.gni and 2138 more.

## browser
1314 changed paths in 3 patch files (36874906 patch bytes).

Paths: chrome/BUILD.gn, chrome/app/app-Info.plist, chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe.vsprops, chrome/app/chrome_exe_main_mac.c, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version, chrome/app/version_assembly/chrome_exe_manifest.template and 1302 more.

## extensions
64 changed paths in 1 patch files (139888 patch bytes).

Paths: extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/storage/storage_frontend.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/app_window/app_web_contents_helper.cc, extensions/browser/app_window/app_window.cc, extensions/browser/app_window/app_window.h, extensions/browser/extension_event_histogram_value.h, extensions/browser/extension_function.cc, extensions/browser/extension_function_histogram_value.h and 52 more.

## components
118 changed paths in 1 patch files (187363 patch bytes).

Paths: components/autofill/content/renderer/autofill_agent.cc, components/autofill/core/browser/personal_data_manager.cc, components/bookmarks.gypi, components/bookmarks/browser/bookmark_codec.cc, components/bookmarks/browser/bookmark_codec.h, components/bookmarks/browser/bookmark_codec_unittest.cc, components/bookmarks/browser/bookmark_index.cc, components/bookmarks/browser/bookmark_match.cc, components/bookmarks/browser/bookmark_match.h, components/bookmarks/browser/bookmark_model.cc, components/bookmarks/browser/bookmark_model.h, components/bookmarks/browser/bookmark_model_unittest.cc and 106 more.

## rendering
132869 changed paths in 260 patch files (849056002 patch bytes).

Paths: content/app/strings/content_strings.gyp, content/browser/browser_main_loop.cc, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc, content/browser/download/download_resource_handler.h and 132857 more.

## ui
43 changed paths in 1 patch files (46069 patch bytes).

Paths: ash/ash_strings.gyp, ash/drag_drop/drag_drop_controller.cc, ash/drag_drop/drag_drop_controller.h, ash/drag_drop/drag_drop_controller_unittest.cc, ash/wm/overview/window_selector_unittest.cc, ui/app_list/test/run_all_unittests.cc, ui/base/BUILD.gn, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/l10n/l10n_util.cc, ui/base/resource/resource_bundle.cc, ui/base/resource/resource_bundle_android.cc and 31 more.

## networking
3 changed paths in 1 patch files (1968 patch bytes).

Paths: net/base/url_util.h, net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc.

## media
126 changed paths in 1 patch files (1156291 patch bytes).

Paths: gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/gpu.gyp, gpu/ipc/service/gpu_channel.cc, gpu/ipc/service/gpu_channel.h, gpu/ipc/service/gpu_channel_manager.h, media/BUILD.gn, media/base/BUILD.gn, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h, media/base/container_names.cc, media/base/container_names.h and 114 more.

## dependencies
79708 changed paths in 198 patch files (1542343202 patch bytes).

Paths: third_party/SPIRV-Tools/src/.clang-format, third_party/SPIRV-Tools/src/.gitignore, third_party/SPIRV-Tools/src/.travis.yml, third_party/SPIRV-Tools/src/CHANGES, third_party/SPIRV-Tools/src/CMakeLists.txt, third_party/SPIRV-Tools/src/LICENSE, third_party/SPIRV-Tools/src/README.md, third_party/SPIRV-Tools/src/external/CMakeLists.txt, third_party/SPIRV-Tools/src/include/spirv-tools/libspirv.h, third_party/SPIRV-Tools/src/include/spirv/GLSL.std.450.h, third_party/SPIRV-Tools/src/include/spirv/OpenCL.std.h, third_party/SPIRV-Tools/src/include/spirv/spirv.h and 79696 more.

## other
3998 changed paths in 8 patch files (56281937 patch bytes).

Paths: .gitattributes, .gitmodules, apps/app_load_service.cc, apps/launcher.cc, base/BUILD.gn, base/base.gyp, base/base_paths.cc, base/base_paths.h, base/base_paths_mac.mm, base/base_paths_posix.cc, base/base_paths_win.cc, base/command_line.cc and 3986 more.
