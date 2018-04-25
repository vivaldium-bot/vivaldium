# Vivaldi 1.14.1077 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `64.0.3282.189` at `9fde53a0d3ec6157ee012caac00cd56fba348c59`.
* Published archive SHA-256: `21cfab74ed2cf01a50692c97b0807098e0d6e3726b41272435131bf9d113c96f`.
* Complete normalized fingerprint: `c5aa2e4f92072af45c1c65a0ac3276099a7fe0b707a08de2e45b027f2d9bd4bc`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.14, announced 2018-01-31): Vivaldi 1.14 – Three years of continuous innovation
Official announcement synopsis: Vivaldi introduces a vertical reader mode (a first for browsers!), Markdown support in Notes, rearrangeable Web Panels and reordering of search
Source: https://vivaldi.com/blog/three-years-of-innovation/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
8807 changed paths in 18 patch files (46272517 patch bytes).

Paths: DEPS, build/android/download_doclava.py, build/branding_value.sh, build/config/BUILDCONFIG.gn, build/config/chrome_build.gni, build/config/compiler/BUILD.gn, build/config/compiler/compiler.gni, build/config/gcc/BUILD.gn, build/config/jumbo.gni, build/config/mac/mac_sdk.gni, build/config/pch.gni, build/git-hooks/pre-commit and 8795 more.

## browser
1373 changed paths in 15 patch files (161857380 patch bytes).

Paths: chrome/BUILD.gn, chrome/android/BUILD.gn, chrome/app/app-Info.plist, chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe_main_mac.cc, chrome/app/chrome_exe_main_win.cc, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version and 1361 more.

## extensions
65 changed paths in 1 patch files (150386 patch bytes).

Paths: extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/file_system/file_system_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.h, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/api/web_request/web_request_api.cc, extensions/browser/app_window/app_web_contents_helper.cc, extensions/browser/app_window/app_window.cc, extensions/browser/app_window/app_window.h, extensions/browser/extension_event_histogram_value.h and 53 more.

## components
187 changed paths in 1 patch files (266023 patch bytes).

Paths: components/autofill/content/browser/content_autofill_driver.cc, components/autofill/content/renderer/autofill_agent.cc, components/autofill/core/browser/personal_data_manager.cc, components/bookmarks/browser/bookmark_codec.cc, components/bookmarks/browser/bookmark_codec.h, components/bookmarks/browser/bookmark_codec_unittest.cc, components/bookmarks/browser/bookmark_model.cc, components/bookmarks/browser/bookmark_model.h, components/bookmarks/browser/bookmark_model_unittest.cc, components/bookmarks/browser/bookmark_node.cc, components/bookmarks/browser/bookmark_node.h, components/bookmarks/browser/bookmark_node_data.cc and 175 more.

## rendering
160688 changed paths in 323 patch files (1101341397 patch bytes).

Paths: content/browser/browser_plugin/browser_plugin_embedder.cc, content/browser/browser_plugin/browser_plugin_embedder.h, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/devtools/render_frame_devtools_agent_host.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc and 160676 more.

## ui
35 changed paths in 1 patch files (42450 patch bytes).

Paths: ui/aura/client/drag_drop_client.cc, ui/aura/client/drag_drop_client.h, ui/base/BUILD.gn, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/dragdrop/drop_target_win.cc, ui/base/l10n/l10n_util.cc, ui/base/resource/resource_bundle.cc, ui/base/resource/resource_bundle_android.cc, ui/base/resource/resource_bundle_mac.mm, ui/events/blink/input_handler_proxy.cc, ui/gfx/ipc/skia/gfx_skia_param_traits.cc and 23 more.

## networking
8 changed paths in 1 patch files (5595 patch bytes).

Paths: net/http/transport_security_state.cc, net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc, services/service_manager/embedder/main.cc, services/ui/public/cpp/gpu/gpu.cc, services/ui/public/cpp/gpu/gpu.h, services/ui/public/interfaces/gpu.mojom, services/ui/ws/gpu_client.h.

## media
61 changed paths in 1 patch files (732898 patch bytes).

Paths: gpu/command_buffer/service/texture_manager.cc, gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/ipc/client/gpu_channel_host.h, gpu/ipc/service/gpu_channel.cc, gpu/ipc/service/gpu_channel.h, media/BUILD.gn, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h, media/base/container_names.cc, media/base/container_names.h, media/base/container_names_unittest.cc and 49 more.

## platforms
2 changed paths in 1 patch files (1656 patch bytes).

Paths: ios/chrome/browser/sessions/ios_chrome_tab_restore_service_client.h, ios/chrome/browser/sessions/ios_chrome_tab_restore_service_client.mm.

## dependencies
91650 changed paths in 223 patch files (1759935460 patch bytes).

Paths: third_party/SPIRV-Tools/src/.clang-format, third_party/SPIRV-Tools/src/.gitignore, third_party/SPIRV-Tools/src/.travis.yml, third_party/SPIRV-Tools/src/CHANGES, third_party/SPIRV-Tools/src/CMakeLists.txt, third_party/SPIRV-Tools/src/LICENSE, third_party/SPIRV-Tools/src/README.md, third_party/SPIRV-Tools/src/external/CMakeLists.txt, third_party/SPIRV-Tools/src/include/spirv-tools/libspirv.h, third_party/SPIRV-Tools/src/include/spirv/GLSL.std.450.h, third_party/SPIRV-Tools/src/include/spirv/OpenCL.std.h, third_party/SPIRV-Tools/src/include/spirv/spirv.h and 91638 more.

## other
2764 changed paths in 6 patch files (30843533 patch bytes).

Paths: .gitattributes, .gitmodules, android_webview/BUILD.gn, apps/launcher.cc, base/android/java/src/org/chromium/base/library_loader/Linker.java, base/base_paths_mac.mm, base/base_paths_posix.cc, base/base_paths_win.cc, base/files/file_util_posix.cc, base/mac/foundation_util.mm, base/memory/shared_memory_posix.cc, base/path_service.cc and 2752 more.
