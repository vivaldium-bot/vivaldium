# Vivaldi 1.8.770 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `57.0.2987.138` at `65f178b70108e995253bda6773e656f583b5e113`.
* Published archive SHA-256: `52087e978ad9a239bfc5161988e8ffee9662a96f456bd7cd4356223936a6e6af`.
* Complete normalized fingerprint: `654238a59f52af9d523ba1d0c4ec443ead499d7135a62bb17fe379fa614ad5a3`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.8, announced 2017-03-29): Vivaldi makes History
Official announcement synopsis: Introducing the new Vivaldi History – a powerful tool that lets you explore your browsing habits and finding previously visited web pages like never
Source: https://vivaldi.com/blog/vivaldi-makes-history/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
2211 changed paths in 5 patch files (9360619 patch bytes).

Paths: DEPS, build/branding_value.sh, build/config/BUILDCONFIG.gn, build/config/chrome_build.gni, build/config/compiler/BUILD.gn, build/config/gcc/BUILD.gn, build/config/mac/mac_sdk.gni, build/config/pch.gni, build/git-hooks/pre-commit, build/mac/copy_framework_unversioned.sh, build/mac/find_sdk.py, build/mac/tweak_info_plist.gni and 2199 more.

## browser
1252 changed paths in 3 patch files (36750505 patch bytes).

Paths: chrome/BUILD.gn, chrome/app/app-Info.plist, chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe_main_mac.c, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version, chrome/app/main_dll_loader_win.cc, chrome/app/version_assembly/chrome_exe_manifest.template and 1240 more.

## extensions
62 changed paths in 1 patch files (148170 patch bytes).

Paths: extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.h, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/storage/storage_frontend.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/app_window/app_web_contents_helper.cc, extensions/browser/app_window/app_window.cc, extensions/browser/app_window/app_window.h, extensions/browser/extension_event_histogram_value.h, extensions/browser/extension_function.cc and 50 more.

## components
174 changed paths in 1 patch files (248028 patch bytes).

Paths: components/autofill/content/renderer/autofill_agent.cc, components/autofill/core/browser/personal_data_manager.cc, components/bookmarks/browser/BUILD.gn, components/bookmarks/browser/bookmark_codec.cc, components/bookmarks/browser/bookmark_codec.h, components/bookmarks/browser/bookmark_codec_unittest.cc, components/bookmarks/browser/bookmark_model.cc, components/bookmarks/browser/bookmark_model.h, components/bookmarks/browser/bookmark_model_unittest.cc, components/bookmarks/browser/bookmark_node.cc, components/bookmarks/browser/bookmark_node.h, components/bookmarks/browser/bookmark_node_data.cc and 162 more.

## rendering
138674 changed paths in 271 patch files (885086680 patch bytes).

Paths: content/browser/browser_main_loop.cc, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc, content/browser/download/download_resource_handler.h, content/browser/frame_host/frame_tree.cc and 138662 more.

## ui
40 changed paths in 1 patch files (42803 patch bytes).

Paths: ash/drag_drop/drag_drop_controller.cc, ash/drag_drop/drag_drop_controller.h, ash/drag_drop/drag_drop_controller_unittest.cc, ash/wm/overview/window_selector_unittest.cc, ui/app_list/test/run_all_unittests.cc, ui/aura/client/drag_drop_client.h, ui/aura/mus/drag_drop_controller_mus.cc, ui/aura/mus/drag_drop_controller_mus.h, ui/base/BUILD.gn, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/l10n/l10n_util.cc and 28 more.

## networking
6 changed paths in 1 patch files (4852 patch bytes).

Paths: net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc, services/ui/public/cpp/gpu/gpu.cc, services/ui/public/cpp/gpu/gpu.h, services/ui/public/interfaces/gpu.mojom, services/ui/ws/gpu_host.cc.

## media
64 changed paths in 1 patch files (188371 patch bytes).

Paths: gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/ipc/client/gpu_channel_host.h, gpu/ipc/service/gpu_channel.cc, gpu/ipc/service/gpu_channel.h, gpu/ipc/service/gpu_channel_manager.h, media/BUILD.gn, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h, media/base/container_names.cc, media/base/container_names.h, media/base/container_names_unittest.cc and 52 more.

## dependencies
83331 changed paths in 212 patch files (1762975527 patch bytes).

Paths: third_party/SPIRV-Tools/src/.clang-format, third_party/SPIRV-Tools/src/.gitignore, third_party/SPIRV-Tools/src/.travis.yml, third_party/SPIRV-Tools/src/CHANGES, third_party/SPIRV-Tools/src/CMakeLists.txt, third_party/SPIRV-Tools/src/LICENSE, third_party/SPIRV-Tools/src/README.md, third_party/SPIRV-Tools/src/external/CMakeLists.txt, third_party/SPIRV-Tools/src/include/spirv-tools/libspirv.h, third_party/SPIRV-Tools/src/include/spirv/GLSL.std.450.h, third_party/SPIRV-Tools/src/include/spirv/OpenCL.std.h, third_party/SPIRV-Tools/src/include/spirv/spirv.h and 83319 more.

## other
3903 changed paths in 8 patch files (55946932 patch bytes).

Paths: .gitattributes, .gitmodules, apps/app_load_service.cc, apps/launcher.cc, base/base_paths_mac.mm, base/base_paths_posix.cc, base/base_paths_win.cc, base/command_line.cc, base/command_line.h, base/files/file_util_posix.cc, base/mac/foundation_util.mm, base/memory/shared_memory_posix.cc and 3891 more.
