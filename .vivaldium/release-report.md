# Vivaldi 1.7.735 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `56.0.2924.88` at `40937ebd47dab9503622964e55b2aa6830c62bb9`.
* Published archive SHA-256: `1b8558b4b4713adaed6b7d5251c38949b33011e223917bc633eefc0d17fcf874`.
* Complete normalized fingerprint: `167c4c19b195b89dadc6c9f793e1b0cfe605232a451bd7d3bccd1b57b7f94843`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.7, announced 2017-02-08): Seize the moment with Vivaldi 1.7
Official announcement synopsis: Packed with new features and improvements, version 1.7 of Vivaldi focuses on various ways of working with screenshots, but there is also much more to
Source: https://vivaldi.com/blog/seize-the-moment-with-vivaldi-1-7/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
2211 changed paths in 5 patch files (9350185 patch bytes).

Paths: DEPS, build/branding_value.sh, build/config/BUILD.gn, build/config/BUILDCONFIG.gn, build/config/chrome_build.gni, build/config/compiler/BUILD.gn, build/config/features.gni, build/config/gcc/BUILD.gn, build/config/mac/mac_sdk.gni, build/git-hooks/pre-commit, build/mac/copy_framework_unversioned.sh, build/mac/find_sdk.py and 2199 more.

## browser
1240 changed paths in 3 patch files (36737827 patch bytes).

Paths: chrome/BUILD.gn, chrome/app/app-Info.plist, chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe_main_mac.c, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version, chrome/app/version_assembly/chrome_exe_manifest.template, chrome/app/version_assembly/version_assembly_manifest.template and 1228 more.

## extensions
60 changed paths in 1 patch files (141139 patch bytes).

Paths: extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/storage/storage_frontend.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/app_window/app_web_contents_helper.cc, extensions/browser/app_window/app_window.cc, extensions/browser/app_window/app_window.h, extensions/browser/extension_event_histogram_value.h, extensions/browser/extension_function.cc, extensions/browser/extension_function_histogram_value.h and 48 more.

## components
97 changed paths in 1 patch files (160846 patch bytes).

Paths: components/autofill/content/renderer/autofill_agent.cc, components/autofill/core/browser/personal_data_manager.cc, components/bookmarks/browser/bookmark_codec.cc, components/bookmarks/browser/bookmark_codec.h, components/bookmarks/browser/bookmark_codec_unittest.cc, components/bookmarks/browser/bookmark_index.cc, components/bookmarks/browser/bookmark_match.cc, components/bookmarks/browser/bookmark_match.h, components/bookmarks/browser/bookmark_model.cc, components/bookmarks/browser/bookmark_model.h, components/bookmarks/browser/bookmark_model_unittest.cc, components/bookmarks/browser/bookmark_node.cc and 85 more.

## rendering
136415 changed paths in 267 patch files (871128187 patch bytes).

Paths: content/browser/browser_main_loop.cc, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc, content/browser/download/download_resource_handler.h, content/browser/frame_host/frame_tree.cc and 136403 more.

## ui
41 changed paths in 1 patch files (43803 patch bytes).

Paths: ash/drag_drop/drag_drop_controller.cc, ash/drag_drop/drag_drop_controller.h, ash/drag_drop/drag_drop_controller_unittest.cc, ash/wm/overview/window_selector_unittest.cc, ui/app_list/test/run_all_unittests.cc, ui/aura/client/drag_drop_client.h, ui/aura/mus/drag_drop_controller_mus.cc, ui/aura/mus/drag_drop_controller_mus.h, ui/base/BUILD.gn, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/l10n/l10n_util.cc and 29 more.

## networking
3 changed paths in 1 patch files (6272 patch bytes).

Paths: net/cert/cert_verify_proc_unittest.cc, net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc.

## media
151 changed paths in 1 patch files (1270978 patch bytes).

Paths: gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/ipc/service/gpu_channel.cc, gpu/ipc/service/gpu_channel.h, gpu/ipc/service/gpu_channel_manager.h, media/BUILD.gn, media/base/BUILD.gn, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h, media/base/audio_discard_helper.cc, media/base/audio_discard_helper.h, media/base/audio_discard_helper_unittest.cc and 139 more.

## dependencies
81464 changed paths in 204 patch files (1539711692 patch bytes).

Paths: third_party/SPIRV-Tools/src/.clang-format, third_party/SPIRV-Tools/src/.gitignore, third_party/SPIRV-Tools/src/.travis.yml, third_party/SPIRV-Tools/src/CHANGES, third_party/SPIRV-Tools/src/CMakeLists.txt, third_party/SPIRV-Tools/src/LICENSE, third_party/SPIRV-Tools/src/README.md, third_party/SPIRV-Tools/src/external/CMakeLists.txt, third_party/SPIRV-Tools/src/include/spirv-tools/libspirv.h, third_party/SPIRV-Tools/src/include/spirv/GLSL.std.450.h, third_party/SPIRV-Tools/src/include/spirv/OpenCL.std.h, third_party/SPIRV-Tools/src/include/spirv/spirv.h and 81452 more.

## other
3918 changed paths in 8 patch files (55948162 patch bytes).

Paths: .gitattributes, .gitmodules, apps/app_load_service.cc, apps/launcher.cc, base/BUILD.gn, base/base_paths_mac.mm, base/base_paths_posix.cc, base/base_paths_win.cc, base/command_line.cc, base/command_line.h, base/features/command_line_feature_reader.cc, base/features/command_line_feature_reader.h and 3906 more.
