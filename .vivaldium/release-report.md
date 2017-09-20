# Vivaldi 1.11.917 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `60.0.3112.105` at `10a0013e13f1ff0ebcae4e1d368ba1a41cc4c9ea`.
* Published archive SHA-256: `4fe713602586cc82e8240e56b1ec87ed2bd34acdaed7438f0076ddc510f1950f`.
* Complete normalized fingerprint: `6074c13ed091e8ee2a5bc9a68dc4c4df8dc0b1bc320f1f449a99826869a3faca`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.11, announced 2017-08-10): Vivaldi 1.11 – Focus on accessibility
Official announcement synopsis: The latest version of the Vivaldi browser is here with improved accessibility options and a brand-new application icon. Read on for the story of Vivaldi
Source: https://vivaldi.com/blog/focus-on-accessibility/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
2276 changed paths in 5 patch files (9695054 patch bytes).

Paths: DEPS, build/branding_value.sh, build/config/BUILDCONFIG.gn, build/config/chrome_build.gni, build/config/compiler/BUILD.gn, build/config/gcc/BUILD.gn, build/config/mac/mac_sdk.gni, build/config/pch.gni, build/git-hooks/pre-commit, build/mac/find_sdk.py, build/mac/tweak_info_plist.gni, build/mac/tweak_info_plist.py and 2264 more.

## browser
1247 changed paths in 3 patch files (36761963 patch bytes).

Paths: chrome/BUILD.gn, chrome/app/app-Info.plist, chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe_main_mac.cc, chrome/app/chrome_exe_main_win.cc, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version, chrome/app/main_dll_loader_win.cc and 1235 more.

## extensions
65 changed paths in 1 patch files (151358 patch bytes).

Paths: extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.h, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/app_window/app_web_contents_helper.cc, extensions/browser/app_window/app_window.cc, extensions/browser/app_window/app_window.h, extensions/browser/extension_event_histogram_value.h, extensions/browser/extension_function.cc, extensions/browser/extension_function_histogram_value.h and 53 more.

## components
173 changed paths in 1 patch files (251870 patch bytes).

Paths: components/autofill/content/renderer/autofill_agent.cc, components/autofill/core/browser/personal_data_manager.cc, components/bookmarks/browser/bookmark_codec.cc, components/bookmarks/browser/bookmark_codec.h, components/bookmarks/browser/bookmark_codec_unittest.cc, components/bookmarks/browser/bookmark_model.cc, components/bookmarks/browser/bookmark_model.h, components/bookmarks/browser/bookmark_model_unittest.cc, components/bookmarks/browser/bookmark_node.cc, components/bookmarks/browser/bookmark_node.h, components/bookmarks/browser/bookmark_node_data.cc, components/bookmarks/browser/bookmark_node_data.h and 161 more.

## rendering
153313 changed paths in 300 patch files (951201440 patch bytes).

Paths: content/browser/browser_main_loop.cc, content/browser/browser_plugin/browser_plugin_embedder.cc, content/browser/browser_plugin/browser_plugin_embedder.h, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc and 153301 more.

## ui
29 changed paths in 1 patch files (31579 patch bytes).

Paths: ui/app_list/test/run_all_unittests.cc, ui/aura/client/drag_drop_client.cc, ui/aura/client/drag_drop_client.h, ui/base/BUILD.gn, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/l10n/l10n_util.cc, ui/base/resource/resource_bundle.cc, ui/base/resource/resource_bundle_mac.mm, ui/shell_dialogs/select_file_dialog_win.cc, ui/views/bubble/bubble_dialog_delegate.cc, ui/views/controls/menu/menu_controller.cc and 17 more.

## networking
10 changed paths in 1 patch files (8172 patch bytes).

Paths: net/http/transport_security_state.cc, net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc, services/service_manager/embedder/main.cc, services/ui/gpu/gpu_service.cc, services/ui/public/cpp/gpu/gpu.cc, services/ui/public/cpp/gpu/gpu.h, services/ui/public/interfaces/gpu.mojom, services/ui/ws/gpu_client.cc, services/ui/ws/gpu_client.h.

## media
65 changed paths in 1 patch files (714881 patch bytes).

Paths: gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/ipc/client/gpu_channel_host.h, gpu/ipc/service/gpu_channel.cc, gpu/ipc/service/gpu_channel.h, gpu/ipc/service/gpu_channel_manager.h, media/BUILD.gn, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h, media/base/container_names.cc, media/base/container_names.h, media/base/container_names_unittest.cc and 53 more.

## platforms
2 changed paths in 1 patch files (1598 patch bytes).

Paths: ios/chrome/browser/sessions/ios_chrome_tab_restore_service_client.h, ios/chrome/browser/sessions/ios_chrome_tab_restore_service_client.mm.

## dependencies
86089 changed paths in 226 patch files (1796757428 patch bytes).

Paths: third_party/SPIRV-Tools/src/.clang-format, third_party/SPIRV-Tools/src/.gitignore, third_party/SPIRV-Tools/src/.travis.yml, third_party/SPIRV-Tools/src/CHANGES, third_party/SPIRV-Tools/src/CMakeLists.txt, third_party/SPIRV-Tools/src/LICENSE, third_party/SPIRV-Tools/src/README.md, third_party/SPIRV-Tools/src/external/CMakeLists.txt, third_party/SPIRV-Tools/src/include/spirv-tools/libspirv.h, third_party/SPIRV-Tools/src/include/spirv/GLSL.std.450.h, third_party/SPIRV-Tools/src/include/spirv/OpenCL.std.h, third_party/SPIRV-Tools/src/include/spirv/spirv.h and 86077 more.

## other
3650 changed paths in 8 patch files (51643698 patch bytes).

Paths: .gitattributes, .gitmodules, apps/launcher.cc, base/base_paths_mac.mm, base/base_paths_posix.cc, base/base_paths_win.cc, base/files/file_util_posix.cc, base/mac/foundation_util.mm, base/memory/shared_memory_posix.cc, base/path_service.cc, base/process/process_win.cc, base/test/launcher/unit_test_launcher.cc and 3638 more.
