# Vivaldi 1.9.818 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `58.0.3029.114` at `2ecbcd0b66b386d6242aa577d4c000d0abc444e6`.
* Published archive SHA-256: `f8e9df688e296c59a6cd4ae8143adfca31f21d0cd84635496ef8e116dd91db4e`.
* Complete normalized fingerprint: `9f0e9013a920c2216a014d83b7c6317dfafe742fd3154bd22fcb170708cee3ca`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.9, announced 2017-04-27): Vivaldi 1.9 – Plant trees as you browse
Official announcement synopsis: Version 1.9 of Vivaldi features the addition of Ecosia – a search engine that plants trees - as well as a number of important security fixes and functional
Source: https://vivaldi.com/blog/plant-trees-with-your-browser/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
2238 changed paths in 5 patch files (9613780 patch bytes).

Paths: DEPS, build/branding_value.sh, build/config/BUILDCONFIG.gn, build/config/chrome_build.gni, build/config/compiler/BUILD.gn, build/config/gcc/BUILD.gn, build/config/mac/mac_sdk.gni, build/config/pch.gni, build/git-hooks/pre-commit, build/mac/copy_framework_unversioned.sh, build/mac/find_sdk.py, build/mac/tweak_info_plist.gni and 2226 more.

## browser
1243 changed paths in 3 patch files (36739384 patch bytes).

Paths: chrome/BUILD.gn, chrome/app/app-Info.plist, chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe_main_mac.c, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version, chrome/app/main_dll_loader_win.cc, chrome/app/vector_icons/BUILD.gn and 1231 more.

## extensions
63 changed paths in 1 patch files (147887 patch bytes).

Paths: extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.h, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/storage/storage_frontend.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/app_window/app_web_contents_helper.cc, extensions/browser/app_window/app_window.cc, extensions/browser/app_window/app_window.h, extensions/browser/extension_event_histogram_value.h, extensions/browser/extension_function.cc and 51 more.

## components
172 changed paths in 1 patch files (247892 patch bytes).

Paths: components/autofill/content/renderer/autofill_agent.cc, components/autofill/core/browser/personal_data_manager.cc, components/bookmarks/browser/bookmark_codec.cc, components/bookmarks/browser/bookmark_codec.h, components/bookmarks/browser/bookmark_codec_unittest.cc, components/bookmarks/browser/bookmark_model.cc, components/bookmarks/browser/bookmark_model.h, components/bookmarks/browser/bookmark_model_unittest.cc, components/bookmarks/browser/bookmark_node.cc, components/bookmarks/browser/bookmark_node.h, components/bookmarks/browser/bookmark_node_data.cc, components/bookmarks/browser/bookmark_node_data.h and 160 more.

## rendering
144568 changed paths in 283 patch files (931437029 patch bytes).

Paths: content/browser/browser_main_loop.cc, content/browser/browser_plugin/browser_plugin_embedder.cc, content/browser/browser_plugin/browser_plugin_embedder.h, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc and 144556 more.

## ui
29 changed paths in 1 patch files (31711 patch bytes).

Paths: ui/app_list/test/run_all_unittests.cc, ui/aura/client/drag_drop_client.cc, ui/aura/client/drag_drop_client.h, ui/base/BUILD.gn, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/l10n/l10n_util.cc, ui/base/resource/resource_bundle.cc, ui/base/resource/resource_bundle_mac.mm, ui/shell_dialogs/select_file_dialog_win.cc, ui/views/bubble/bubble_dialog_delegate.cc, ui/views/controls/menu/menu_controller.cc and 17 more.

## networking
8 changed paths in 1 patch files (6863 patch bytes).

Paths: net/cert/cert_verify_proc_unittest.cc, net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc, services/ui/gpu/gpu_service.cc, services/ui/public/cpp/gpu/gpu.cc, services/ui/public/cpp/gpu/gpu.h, services/ui/public/interfaces/gpu.mojom, services/ui/ws/gpu_host.cc.

## media
64 changed paths in 1 patch files (753948 patch bytes).

Paths: gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/ipc/client/gpu_channel_host.h, gpu/ipc/service/gpu_channel.h, gpu/ipc/service/gpu_channel_manager.h, media/BUILD.gn, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h, media/base/container_names.cc, media/base/container_names.h, media/base/container_names_unittest.cc, media/base/decoder_buffer.h and 52 more.

## dependencies
84653 changed paths in 217 patch files (1751633628 patch bytes).

Paths: third_party/SPIRV-Tools/src/.clang-format, third_party/SPIRV-Tools/src/.gitignore, third_party/SPIRV-Tools/src/.travis.yml, third_party/SPIRV-Tools/src/CHANGES, third_party/SPIRV-Tools/src/CMakeLists.txt, third_party/SPIRV-Tools/src/LICENSE, third_party/SPIRV-Tools/src/README.md, third_party/SPIRV-Tools/src/external/CMakeLists.txt, third_party/SPIRV-Tools/src/include/spirv-tools/libspirv.h, third_party/SPIRV-Tools/src/include/spirv/GLSL.std.450.h, third_party/SPIRV-Tools/src/include/spirv/OpenCL.std.h, third_party/SPIRV-Tools/src/include/spirv/spirv.h and 84641 more.

## other
3903 changed paths in 8 patch files (55985100 patch bytes).

Paths: .gitattributes, .gitmodules, apps/app_load_service.cc, apps/launcher.cc, base/base_paths_mac.mm, base/base_paths_posix.cc, base/base_paths_win.cc, base/files/file_util_posix.cc, base/mac/foundation_util.mm, base/memory/shared_memory_posix.cc, base/path_service.cc, base/process/process_win.cc and 3891 more.
