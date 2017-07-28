# Vivaldi 1.10.867 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `59.0.3071.112` at `2404cfa2d19395ef9126167e811014e1df44e3cc`.
* Published archive SHA-256: `1b7ea5824a4852993ebf1dab884e6da7093c8ddf0bbdc309faea5290c576a09c`.
* Complete normalized fingerprint: `04cdf292efa1fa25169597eb1ffa70683e5828892959b567da13abeccd244360`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.10, announced 2017-06-15): Vivaldi powers up the Start Page and adds docked Dev Tools
Official announcement synopsis: Just browsing is yesterday. Make it personal with Vivaldi
Source: https://vivaldi.com/blog/powering-up-the-start-page/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
2240 changed paths in 5 patch files (9617431 patch bytes).

Paths: DEPS, build/branding_value.sh, build/config/BUILDCONFIG.gn, build/config/chrome_build.gni, build/config/compiler/BUILD.gn, build/config/gcc/BUILD.gn, build/config/mac/mac_sdk.gni, build/config/pch.gni, build/git-hooks/pre-commit, build/mac/find_sdk.py, build/mac/tweak_info_plist.gni, build/mac/tweak_info_plist.py and 2228 more.

## browser
1247 changed paths in 3 patch files (36758118 patch bytes).

Paths: chrome/BUILD.gn, chrome/app/app-Info.plist, chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe_main_mac.c, chrome/app/chrome_exe_main_win.cc, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version, chrome/app/main_dll_loader_win.cc and 1235 more.

## extensions
70 changed paths in 1 patch files (153669 patch bytes).

Paths: extensions/browser/api/BUILD.gn, extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/guest_view/BUILD.gn, extensions/browser/api/guest_view/app_view/BUILD.gn, extensions/browser/api/guest_view/extension_view/BUILD.gn, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.h, extensions/browser/api/guest_view/web_view/BUILD.gn, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/app_window/app_web_contents_helper.cc and 58 more.

## components
173 changed paths in 1 patch files (251721 patch bytes).

Paths: components/autofill/content/renderer/autofill_agent.cc, components/autofill/core/browser/personal_data_manager.cc, components/bookmarks/browser/bookmark_codec.cc, components/bookmarks/browser/bookmark_codec.h, components/bookmarks/browser/bookmark_codec_unittest.cc, components/bookmarks/browser/bookmark_model.cc, components/bookmarks/browser/bookmark_model.h, components/bookmarks/browser/bookmark_model_unittest.cc, components/bookmarks/browser/bookmark_node.cc, components/bookmarks/browser/bookmark_node.h, components/bookmarks/browser/bookmark_node_data.cc, components/bookmarks/browser/bookmark_node_data.h and 161 more.

## rendering
149295 changed paths in 292 patch files (989203686 patch bytes).

Paths: content/browser/browser_main_loop.cc, content/browser/browser_plugin/browser_plugin_embedder.cc, content/browser/browser_plugin/browser_plugin_embedder.h, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc and 149283 more.

## ui
29 changed paths in 1 patch files (31562 patch bytes).

Paths: ui/app_list/test/run_all_unittests.cc, ui/aura/client/drag_drop_client.cc, ui/aura/client/drag_drop_client.h, ui/base/BUILD.gn, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/l10n/l10n_util.cc, ui/base/resource/resource_bundle.cc, ui/base/resource/resource_bundle_mac.mm, ui/shell_dialogs/select_file_dialog_win.cc, ui/views/bubble/bubble_dialog_delegate.cc, ui/views/controls/menu/menu_controller.cc and 17 more.

## networking
10 changed paths in 1 patch files (8645 patch bytes).

Paths: net/http/transport_security_state.cc, net/ssl/client_cert_store_unittest-inl.h, net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc, services/ui/gpu/gpu_service.cc, services/ui/public/cpp/gpu/gpu.cc, services/ui/public/cpp/gpu/gpu.h, services/ui/public/interfaces/gpu.mojom, services/ui/ws/gpu_client.cc, services/ui/ws/gpu_client.h.

## media
64 changed paths in 1 patch files (757794 patch bytes).

Paths: gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/ipc/client/gpu_channel_host.h, gpu/ipc/service/gpu_channel.h, gpu/ipc/service/gpu_channel_manager.h, media/BUILD.gn, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h, media/base/container_names.cc, media/base/container_names.h, media/base/container_names_unittest.cc, media/base/decoder_buffer.h and 52 more.

## platforms
2 changed paths in 1 patch files (1598 patch bytes).

Paths: ios/chrome/browser/sessions/ios_chrome_tab_restore_service_client.h, ios/chrome/browser/sessions/ios_chrome_tab_restore_service_client.mm.

## dependencies
85202 changed paths in 225 patch files (1763629441 patch bytes).

Paths: third_party/SPIRV-Tools/src/.clang-format, third_party/SPIRV-Tools/src/.gitignore, third_party/SPIRV-Tools/src/.travis.yml, third_party/SPIRV-Tools/src/CHANGES, third_party/SPIRV-Tools/src/CMakeLists.txt, third_party/SPIRV-Tools/src/LICENSE, third_party/SPIRV-Tools/src/README.md, third_party/SPIRV-Tools/src/external/CMakeLists.txt, third_party/SPIRV-Tools/src/include/spirv-tools/libspirv.h, third_party/SPIRV-Tools/src/include/spirv/GLSL.std.450.h, third_party/SPIRV-Tools/src/include/spirv/OpenCL.std.h, third_party/SPIRV-Tools/src/include/spirv/spirv.h and 85190 more.

## other
3907 changed paths in 8 patch files (56055251 patch bytes).

Paths: .gitattributes, .gitmodules, apps/launcher.cc, base/base_paths_mac.mm, base/base_paths_posix.cc, base/base_paths_win.cc, base/files/file_util_posix.cc, base/mac/foundation_util.mm, base/memory/shared_memory_posix.cc, base/path_service.cc, base/process/process_win.cc, base/test/launcher/unit_test_launcher.cc and 3895 more.
