# Vivaldi 1.12.955 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `61.0.3163.102` at `643062ea4655e25f7f464678a8c730bd9b668480`.
* Published archive SHA-256: `cfd1003bbc586edad297e6c15687880faa57009367197f8ab541f6361b9ef909`.
* Complete normalized fingerprint: `a9af8389865716064a446b69a76d03aaaecd43093a08ae9ff020af9c1f3c86c6`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.12, announced 2017-09-20): Vivaldi 1.12 – Giving you the browser you want
Official announcement synopsis: The latest version of Vivaldi is here, featuring three requests that may ring a bell. Why? Because they came from
Source: https://vivaldi.com/blog/the-browser-you-want/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
8644 changed paths in 17 patch files (45121968 patch bytes).

Paths: DEPS, build/branding_value.sh, build/config/BUILDCONFIG.gn, build/config/chrome_build.gni, build/config/compiler/BUILD.gn, build/config/gcc/BUILD.gn, build/config/jumbo.gni, build/config/mac/mac_sdk.gni, build/config/merge_for_jumbo.py, build/config/pch.gni, build/git-hooks/pre-commit, build/mac/find_sdk.py and 8632 more.

## browser
1265 changed paths in 3 patch files (36795797 patch bytes).

Paths: chrome/BUILD.gn, chrome/app/app-Info.plist, chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe_main_mac.cc, chrome/app/chrome_exe_main_win.cc, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version, chrome/app/generated_resources.grd and 1253 more.

## extensions
66 changed paths in 1 patch files (152018 patch bytes).

Paths: extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.h, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/app_window/app_web_contents_helper.cc, extensions/browser/app_window/app_window.cc, extensions/browser/app_window/app_window.h, extensions/browser/extension_event_histogram_value.h, extensions/browser/extension_function.cc, extensions/browser/extension_function_histogram_value.h and 54 more.

## components
177 changed paths in 1 patch files (258215 patch bytes).

Paths: components/autofill/content/renderer/autofill_agent.cc, components/autofill/core/browser/personal_data_manager.cc, components/bookmarks/browser/bookmark_codec.cc, components/bookmarks/browser/bookmark_codec.h, components/bookmarks/browser/bookmark_codec_unittest.cc, components/bookmarks/browser/bookmark_model.cc, components/bookmarks/browser/bookmark_model.h, components/bookmarks/browser/bookmark_model_unittest.cc, components/bookmarks/browser/bookmark_node.cc, components/bookmarks/browser/bookmark_node.h, components/bookmarks/browser/bookmark_node_data.cc, components/bookmarks/browser/bookmark_node_data.h and 165 more.

## rendering
154223 changed paths in 302 patch files (1008705567 patch bytes).

Paths: content/browser/browser_plugin/browser_plugin_embedder.cc, content/browser/browser_plugin/browser_plugin_embedder.h, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc, content/browser/download/download_resource_handler.h and 154211 more.

## ui
31 changed paths in 1 patch files (36363 patch bytes).

Paths: ui/app_list/app_list_features.cc, ui/app_list/app_list_features.h, ui/app_list/views/search_result_tile_item_list_view_unittest.cc, ui/aura/client/drag_drop_client.cc, ui/aura/client/drag_drop_client.h, ui/base/BUILD.gn, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/l10n/l10n_util.cc, ui/base/resource/resource_bundle.cc, ui/base/resource/resource_bundle_mac.mm, ui/shell_dialogs/select_file_dialog_win.cc and 19 more.

## networking
10 changed paths in 1 patch files (8543 patch bytes).

Paths: net/http/transport_security_state.cc, net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc, services/service_manager/embedder/main.cc, services/ui/gpu/gpu_service.cc, services/ui/gpu/gpu_service.h, services/ui/public/cpp/gpu/gpu.cc, services/ui/public/cpp/gpu/gpu.h, services/ui/public/interfaces/gpu.mojom, services/ui/ws/gpu_client.h.

## media
60 changed paths in 1 patch files (731545 patch bytes).

Paths: gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/ipc/client/gpu_channel_host.h, gpu/ipc/service/gpu_channel.cc, gpu/ipc/service/gpu_channel.h, media/BUILD.gn, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h, media/base/container_names.cc, media/base/container_names.h, media/base/container_names_unittest.cc, media/base/decoder_buffer.h and 48 more.

## platforms
2 changed paths in 1 patch files (1598 patch bytes).

Paths: ios/chrome/browser/sessions/ios_chrome_tab_restore_service_client.h, ios/chrome/browser/sessions/ios_chrome_tab_restore_service_client.mm.

## dependencies
87985 changed paths in 225 patch files (1813580364 patch bytes).

Paths: third_party/SPIRV-Tools/src/.clang-format, third_party/SPIRV-Tools/src/.gitignore, third_party/SPIRV-Tools/src/.travis.yml, third_party/SPIRV-Tools/src/CHANGES, third_party/SPIRV-Tools/src/CMakeLists.txt, third_party/SPIRV-Tools/src/LICENSE, third_party/SPIRV-Tools/src/README.md, third_party/SPIRV-Tools/src/external/CMakeLists.txt, third_party/SPIRV-Tools/src/include/spirv-tools/libspirv.h, third_party/SPIRV-Tools/src/include/spirv/GLSL.std.450.h, third_party/SPIRV-Tools/src/include/spirv/OpenCL.std.h, third_party/SPIRV-Tools/src/include/spirv/spirv.h and 87973 more.

## other
3647 changed paths in 8 patch files (51646407 patch bytes).

Paths: .gitattributes, .gitmodules, apps/launcher.cc, base/base_paths_mac.mm, base/base_paths_posix.cc, base/base_paths_win.cc, base/files/file_util_posix.cc, base/mac/foundation_util.mm, base/memory/shared_memory_posix.cc, base/path_service.cc, base/process/process_win.cc, base/test/launcher/unit_test_launcher.cc and 3635 more.
