# Vivaldi 1.13.1008 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `62.0.3202.97` at `03210a6f8e3984997ecf5c1c4ca7bb6100a407ca`.
* Published archive SHA-256: `d8a839c655762ea9912c1fb0c21c0295d1ad14d738f9dfb46fddae7c75841f97`.
* Complete normalized fingerprint: `e8db07627a72c3030aa96e056e629e34387bfad4a66861cdcbd12ba961d7a11e`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.13, announced 2017-11-22): Vivaldi 1.13 adds Window Panel, improves Downloads and brings under-the-hood enhancements
Official announcement synopsis: The Window Panel makes a debut in our latest version, together with improved downloads and under-the-hood
Source: https://vivaldi.com/blog/vivaldi-1-13-adds-window-panel/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
8717 changed paths in 18 patch files (45804974 patch bytes).

Paths: DEPS, build/android/download_doclava.py, build/branding_value.sh, build/config/BUILDCONFIG.gn, build/config/chrome_build.gni, build/config/compiler/BUILD.gn, build/config/gcc/BUILD.gn, build/config/ios/rules.gni, build/config/mac/mac_sdk.gni, build/config/mac/plist_util.py, build/config/mac/rules.gni, build/config/pch.gni and 8705 more.

## browser
1360 changed paths in 3 patch files (58531362 patch bytes).

Paths: chrome/BUILD.gn, chrome/android/BUILD.gn, chrome/app/app-Info.plist, chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe_main_mac.cc, chrome/app/chrome_exe_main_win.cc, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version and 1348 more.

## extensions
67 changed paths in 1 patch files (152280 patch bytes).

Paths: extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/file_system/file_system_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.h, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/app_window/app_web_contents_helper.cc, extensions/browser/app_window/app_window.cc, extensions/browser/app_window/app_window.h, extensions/browser/extension_event_histogram_value.h, extensions/browser/extension_function.cc and 55 more.

## components
185 changed paths in 1 patch files (271166 patch bytes).

Paths: components/autofill/content/renderer/autofill_agent.cc, components/autofill/core/browser/personal_data_manager.cc, components/bookmarks/browser/bookmark_codec.cc, components/bookmarks/browser/bookmark_codec.h, components/bookmarks/browser/bookmark_codec_unittest.cc, components/bookmarks/browser/bookmark_model.cc, components/bookmarks/browser/bookmark_model.h, components/bookmarks/browser/bookmark_model_unittest.cc, components/bookmarks/browser/bookmark_node.cc, components/bookmarks/browser/bookmark_node.h, components/bookmarks/browser/bookmark_node_data.cc, components/bookmarks/browser/bookmark_node_data.h and 173 more.

## rendering
157570 changed paths in 308 patch files (1019720151 patch bytes).

Paths: content/browser/browser_plugin/browser_plugin_embedder.cc, content/browser/browser_plugin/browser_plugin_embedder.h, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc, content/browser/download/download_resource_handler.h and 157558 more.

## ui
32 changed paths in 1 patch files (35763 patch bytes).

Paths: ui/aura/client/drag_drop_client.cc, ui/aura/client/drag_drop_client.h, ui/base/BUILD.gn, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/dragdrop/drop_target_win.cc, ui/base/l10n/l10n_util.cc, ui/base/resource/resource_bundle.cc, ui/base/resource/resource_bundle_android.cc, ui/base/resource/resource_bundle_mac.mm, ui/events/blink/input_handler_proxy.cc, ui/message_center/message_center_tray_unittest.cc and 20 more.

## networking
10 changed paths in 1 patch files (8050 patch bytes).

Paths: net/http/transport_security_state.cc, net/quic/core/quic_stream_sequencer_buffer.cc, net/quic/core/quic_stream_sequencer_buffer_test.cc, net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc, services/service_manager/embedder/main.cc, services/ui/public/cpp/gpu/gpu.cc, services/ui/public/cpp/gpu/gpu.h, services/ui/public/interfaces/gpu.mojom, services/ui/ws/gpu_client.h.

## media
65 changed paths in 1 patch files (735948 patch bytes).

Paths: gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/config/gpu_test_config.cc, gpu/config/gpu_test_config.h, gpu/config/gpu_test_expectations_parser.cc, gpu/config/gpu_test_expectations_parser_unittest.cc, gpu/ipc/client/gpu_channel_host.h, gpu/ipc/service/gpu_channel.cc, gpu/ipc/service/gpu_channel.h, media/BUILD.gn, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h and 53 more.

## platforms
3 changed paths in 1 patch files (2390 patch bytes).

Paths: ios/chrome/browser/sessions/ios_chrome_tab_restore_service_client.h, ios/chrome/browser/sessions/ios_chrome_tab_restore_service_client.mm, ios/third_party/material_components_ios/BUILD.gn.

## dependencies
88157 changed paths in 229 patch files (1816080174 patch bytes).

Paths: third_party/SPIRV-Tools/src/.clang-format, third_party/SPIRV-Tools/src/.gitignore, third_party/SPIRV-Tools/src/.travis.yml, third_party/SPIRV-Tools/src/CHANGES, third_party/SPIRV-Tools/src/CMakeLists.txt, third_party/SPIRV-Tools/src/LICENSE, third_party/SPIRV-Tools/src/README.md, third_party/SPIRV-Tools/src/external/CMakeLists.txt, third_party/SPIRV-Tools/src/include/spirv-tools/libspirv.h, third_party/SPIRV-Tools/src/include/spirv/GLSL.std.450.h, third_party/SPIRV-Tools/src/include/spirv/OpenCL.std.h, third_party/SPIRV-Tools/src/include/spirv/spirv.h and 88145 more.

## other
3648 changed paths in 8 patch files (51656004 patch bytes).

Paths: .gitattributes, .gitmodules, android_webview/BUILD.gn, apps/launcher.cc, base/android/java/src/org/chromium/base/library_loader/Linker.java, base/base_paths_mac.mm, base/base_paths_posix.cc, base/base_paths_win.cc, base/files/file_util_posix.cc, base/mac/foundation_util.mm, base/memory/shared_memory_posix.cc, base/path_service.cc and 3636 more.
