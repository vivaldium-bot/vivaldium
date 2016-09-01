# Vivaldi 1.3.551 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `52.0.2743.117` at `72334afec5c1869f45fafaa654e70b92b686d508`.
* Published archive SHA-256: `0979bfdac9e13c2661ffff8036947ea8d01340965a1d2c358ab32c4db6b2b142`.
* Complete normalized fingerprint: `538b8516a4977a6cc84d26142518d1892c89331b80a9a70c24594b23eaa37399`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.3, announced 2016-08-11): Vivaldi version 1.3 debuts with custom browser themes, enhanced privacy and much more
Official announcement synopsis: Custom browser themes make their debut in Vivaldi 1.3 along with enhanced privacy and much more. The most customizable browser is now the most
Source: https://vivaldi.com/blog/browser-themes-debut-in-vivaldi-version-1-3/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
2050 changed paths in 5 patch files (7635414 patch bytes).

Paths: DEPS, build/branding_value.sh, build/chrome_settings.gypi, build/common.gypi, build/git-hooks/pre-commit, build/gyp_chromium.py, build/install-build-deps.sh, build/json_schema_bundle_compile.gypi, build/json_schema_bundle_registration_compile.gypi, build/json_schema_compile.gypi, build/mac/copy_framework_unversioned.sh, build/mac/tweak_info_plist.py and 2038 more.

## browser
1291 changed paths in 3 patch files (36834936 patch bytes).

Paths: chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe.vsprops, chrome/app/chrome_exe_main_mac.c, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version, chrome/app/version_assembly/chrome_exe_manifest.template, chrome/app/version_assembly/chrome_exe_manifest_action.gypi, chrome/app/version_assembly/version_assembly_manifest.template and 1279 more.

## extensions
64 changed paths in 1 patch files (135044 patch bytes).

Paths: extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/storage/storage_frontend.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/app_window/app_web_contents_helper.cc, extensions/browser/app_window/app_window.cc, extensions/browser/app_window/app_window.h, extensions/browser/extension_event_histogram_value.h, extensions/browser/extension_function.cc, extensions/browser/extension_function_histogram_value.h and 52 more.

## components
114 changed paths in 1 patch files (181929 patch bytes).

Paths: components/autofill/core/browser/personal_data_manager.cc, components/bookmarks.gypi, components/bookmarks/browser/bookmark_codec.cc, components/bookmarks/browser/bookmark_codec.h, components/bookmarks/browser/bookmark_codec_unittest.cc, components/bookmarks/browser/bookmark_index.cc, components/bookmarks/browser/bookmark_match.cc, components/bookmarks/browser/bookmark_match.h, components/bookmarks/browser/bookmark_model.cc, components/bookmarks/browser/bookmark_model.h, components/bookmarks/browser/bookmark_model_unittest.cc, components/bookmarks/browser/bookmark_node.cc and 102 more.

## rendering
131458 changed paths in 257 patch files (836720465 patch bytes).

Paths: content/app/strings/content_strings.gyp, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc, content/browser/download/download_resource_handler.h, content/browser/frame_host/frame_tree.cc and 131446 more.

## ui
41 changed paths in 1 patch files (44526 patch bytes).

Paths: ash/ash_strings.gyp, ash/drag_drop/drag_drop_controller.cc, ash/drag_drop/drag_drop_controller.h, ash/drag_drop/drag_drop_controller_unittest.cc, ash/wm/overview/window_selector_unittest.cc, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/l10n/l10n_util.cc, ui/base/resource/resource_bundle.cc, ui/base/resource/resource_bundle_android.cc, ui/base/resource/resource_bundle_ios.mm, ui/base/resource/resource_bundle_mac.mm and 29 more.

## networking
3 changed paths in 1 patch files (1969 patch bytes).

Paths: net/base/url_util.h, net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc.

## media
121 changed paths in 1 patch files (1092416 patch bytes).

Paths: gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/gpu.gyp, gpu/ipc/service/gpu_channel.cc, gpu/ipc/service/gpu_channel.h, gpu/ipc/service/gpu_channel_manager.h, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h, media/base/container_names.cc, media/base/container_names.h, media/base/container_names_unittest.cc, media/base/decoder_buffer.h and 109 more.

## dependencies
64490 changed paths in 183 patch files (1589307416 patch bytes).

Paths: third_party/SPIRV-Tools/src/.clang-format, third_party/SPIRV-Tools/src/.gitignore, third_party/SPIRV-Tools/src/.travis.yml, third_party/SPIRV-Tools/src/CHANGES, third_party/SPIRV-Tools/src/CMakeLists.txt, third_party/SPIRV-Tools/src/LICENSE, third_party/SPIRV-Tools/src/README.md, third_party/SPIRV-Tools/src/external/CMakeLists.txt, third_party/SPIRV-Tools/src/include/spirv-tools/libspirv.h, third_party/SPIRV-Tools/src/include/spirv/GLSL.std.450.h, third_party/SPIRV-Tools/src/include/spirv/OpenCL.std.h, third_party/SPIRV-Tools/src/include/spirv/spirv.h and 64478 more.

## other
4039 changed paths in 8 patch files (57899701 patch bytes).

Paths: .gitattributes, .gitmodules, apps/app_load_service.cc, apps/launcher.cc, base/base.gyp, base/base.gypi, base/base_paths.cc, base/base_paths.h, base/base_paths_mac.mm, base/base_paths_posix.cc, base/base_paths_win.cc, base/command_line.cc and 4027 more.
