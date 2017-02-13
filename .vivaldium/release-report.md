# Vivaldi 1.6.689 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `55.0.2883.98` at `52680a3f64982cdceac0345ff3bf8e1878ca7ea5`.
* Published archive SHA-256: `dcdd12cd7088bc887a8171ea872ca2c892cd9040572b2a4d857f93bbcc6fd0fc`.
* Complete normalized fingerprint: `e7176bda39b03a0a453708881f5803bee7a8d0f345bf3f26deee03d08914c54c`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.6, announced 2016-12-15): Details matter. Vivaldi 1.6 is ready
Official announcement synopsis: The best products do two things well: Features and details. Features are what draw people to the product and details are what keep them
Source: https://vivaldi.com/blog/details-matter-vivaldi-1-6-is-ready-2/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
2192 changed paths in 5 patch files (9142077 patch bytes).

Paths: BUILD.gn, DEPS, build/branding_value.sh, build/config/BUILD.gn, build/config/BUILDCONFIG.gn, build/config/chrome_build.gni, build/config/compiler/BUILD.gn, build/config/features.gni, build/config/gcc/BUILD.gn, build/config/mac/mac_sdk.gni, build/git-hooks/pre-commit, build/json_schema_api.gni and 2180 more.

## browser
1284 changed paths in 3 patch files (36797688 patch bytes).

Paths: chrome/BUILD.gn, chrome/app/app-Info.plist, chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe.vsprops, chrome/app/chrome_exe_main_mac.c, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version, chrome/app/version_assembly/chrome_exe_manifest.template and 1272 more.

## extensions
61 changed paths in 1 patch files (139506 patch bytes).

Paths: extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/storage/storage_frontend.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/app_window/app_web_contents_helper.cc, extensions/browser/app_window/app_window.cc, extensions/browser/app_window/app_window.h, extensions/browser/extension_event_histogram_value.h, extensions/browser/extension_function.cc, extensions/browser/extension_function_histogram_value.h and 49 more.

## components
110 changed paths in 1 patch files (179653 patch bytes).

Paths: components/autofill/content/renderer/autofill_agent.cc, components/autofill/core/browser/personal_data_manager.cc, components/bookmarks/browser/bookmark_codec.cc, components/bookmarks/browser/bookmark_codec.h, components/bookmarks/browser/bookmark_codec_unittest.cc, components/bookmarks/browser/bookmark_index.cc, components/bookmarks/browser/bookmark_match.cc, components/bookmarks/browser/bookmark_match.h, components/bookmarks/browser/bookmark_model.cc, components/bookmarks/browser/bookmark_model.h, components/bookmarks/browser/bookmark_model_unittest.cc, components/bookmarks/browser/bookmark_node.cc and 98 more.

## rendering
133443 changed paths in 261 patch files (863721099 patch bytes).

Paths: content/browser/browser_main_loop.cc, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc, content/browser/download/download_resource_handler.h, content/browser/frame_host/frame_tree.cc and 133431 more.

## ui
41 changed paths in 1 patch files (45249 patch bytes).

Paths: ash/drag_drop/drag_drop_controller.cc, ash/drag_drop/drag_drop_controller.h, ash/drag_drop/drag_drop_controller_unittest.cc, ash/wm/overview/window_selector_unittest.cc, ui/app_list/test/run_all_unittests.cc, ui/base/BUILD.gn, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/l10n/l10n_util.cc, ui/base/resource/resource_bundle.cc, ui/base/resource/resource_bundle_android.cc, ui/base/resource/resource_bundle_ios.mm and 29 more.

## networking
3 changed paths in 1 patch files (1982 patch bytes).

Paths: net/base/url_util.h, net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc.

## media
122 changed paths in 1 patch files (1153131 patch bytes).

Paths: gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/ipc/service/gpu_channel.cc, gpu/ipc/service/gpu_channel.h, gpu/ipc/service/gpu_channel_manager.h, media/BUILD.gn, media/base/BUILD.gn, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h, media/base/container_names.cc, media/base/container_names.h, media/base/container_names_unittest.cc and 110 more.

## dependencies
80342 changed paths in 204 patch files (1570635931 patch bytes).

Paths: third_party/SPIRV-Tools/src/.clang-format, third_party/SPIRV-Tools/src/.gitignore, third_party/SPIRV-Tools/src/.travis.yml, third_party/SPIRV-Tools/src/CHANGES, third_party/SPIRV-Tools/src/CMakeLists.txt, third_party/SPIRV-Tools/src/LICENSE, third_party/SPIRV-Tools/src/README.md, third_party/SPIRV-Tools/src/external/CMakeLists.txt, third_party/SPIRV-Tools/src/include/spirv-tools/libspirv.h, third_party/SPIRV-Tools/src/include/spirv/GLSL.std.450.h, third_party/SPIRV-Tools/src/include/spirv/OpenCL.std.h, third_party/SPIRV-Tools/src/include/spirv/spirv.h and 80330 more.

## other
3941 changed paths in 8 patch files (55997767 patch bytes).

Paths: .gitattributes, .gitmodules, apps/app_load_service.cc, apps/launcher.cc, base/BUILD.gn, base/base_paths.cc, base/base_paths.h, base/base_paths_mac.mm, base/base_paths_posix.cc, base/base_paths_win.cc, base/command_line.cc, base/command_line.h and 3929 more.
