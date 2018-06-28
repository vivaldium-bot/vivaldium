# Vivaldi 1.15.1147 reconstructed release

This is reconstructed publication history. Original Vivaldi commit boundaries, messages, dates, and individual authors are unavailable. Intermediate synthetic commits are not claimed buildable; this tag is the verified reconstruction boundary.

* Chromium base: `65.0.3325.183` at `c8a0e12fcb29b865a57eb237a974b22874804852`.
* Published archive SHA-256: `d82c2623af7951e981ee9548755996822d824ce6853af32160112038a9ecaa33`.
* Complete normalized fingerprint: `c9c4bddcabb951e9a46addbf515eae5692bfe357dabf69f5859cc92316311e2a`.
* Published dependency files absent from the selected Chromium superproject are retained as patch additions; this does not imply Vivaldi authorship.

## Published release context

Release context (family 1.15, announced 2018-04-25): Vivaldi 1.15 : Just Better.
Official announcement synopsis: Vivaldi launches version 1.15 of its browser, giving you even more control over the appearance and fine-tuning key features like Bookmarks and
Source: https://vivaldi.com/blog/vivaldi-1-15-just-better/
This is inferred release-level context. These references do not identify original commits or prove that a feature belongs to this synthetic commit.

## build
8806 changed paths in 18 patch files (46278471 patch bytes).

Paths: DEPS, build/android/download_doclava.py, build/branding_value.sh, build/config/BUILDCONFIG.gn, build/config/chrome_build.gni, build/config/compiler/BUILD.gn, build/config/compiler/compiler.gni, build/config/gcc/BUILD.gn, build/config/mac/mac_sdk.gni, build/git-hooks/pre-commit, build/gn_chromium.py, build/install-build-deps.sh and 8794 more.

## browser
1382 changed paths in 16 patch files (161904110 patch bytes).

Paths: chrome/BUILD.gn, chrome/android/BUILD.gn, chrome/app/app-Info.plist, chrome/app/chrome_dll.rc, chrome/app/chrome_dll.ver, chrome/app/chrome_exe.rc, chrome/app/chrome_exe.ver, chrome/app/chrome_exe_main_mac.cc, chrome/app/chrome_exe_main_win.cc, chrome/app/chrome_main.cc, chrome/app/chrome_main_delegate.cc, chrome/app/chrome_version.rc.version and 1370 more.

## extensions
68 changed paths in 1 patch files (158991 patch bytes).

Paths: extensions/browser/api/app_window/app_window_api.cc, extensions/browser/api/file_system/file_system_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.cc, extensions/browser/api/guest_view/guest_view_internal_api.h, extensions/browser/api/guest_view/web_view/web_view_internal_api.cc, extensions/browser/api/management/management_api.cc, extensions/browser/api/web_contents_capture_client.cc, extensions/browser/app_window/app_web_contents_helper.cc, extensions/browser/app_window/app_window.cc, extensions/browser/app_window/app_window.h, extensions/browser/extension_event_histogram_value.h, extensions/browser/extension_function.cc and 56 more.

## components
207 changed paths in 1 patch files (314252 patch bytes).

Paths: components/autofill/content/browser/content_autofill_driver.cc, components/autofill/core/browser/autofill_manager.cc, components/autofill/core/browser/personal_data_manager.cc, components/autofill/core/browser/personal_data_manager.h, components/autofill/core/browser/webdata/autofill_table.cc, components/autofill/core/browser/webdata/autofill_table.h, components/autofill/core/browser/webdata/autofill_table_unittest.cc, components/autofill/core/browser/webdata/autofill_webdata.h, components/autofill/core/browser/webdata/autofill_webdata_backend_impl.cc, components/autofill/core/browser/webdata/autofill_webdata_backend_impl.h, components/autofill/core/browser/webdata/autofill_webdata_service.cc, components/autofill/core/browser/webdata/autofill_webdata_service.h and 195 more.

## rendering
162860 changed paths in 329 patch files (1123121743 patch bytes).

Paths: content/browser/browser_plugin/browser_plugin_embedder.cc, content/browser/browser_plugin/browser_plugin_embedder.h, content/browser/browser_plugin/browser_plugin_guest.cc, content/browser/browser_plugin/browser_plugin_guest.h, content/browser/child_process_security_policy_impl.cc, content/browser/devtools/devtools_http_handler.cc, content/browser/download/download_create_info.cc, content/browser/download/download_create_info.h, content/browser/download/download_item_impl.cc, content/browser/download/download_request_core.cc, content/browser/download/download_request_core.h, content/browser/download/download_resource_handler.cc and 162848 more.

## ui
39 changed paths in 1 patch files (44636 patch bytes).

Paths: ui/aura/client/drag_drop_client.cc, ui/aura/client/drag_drop_client.h, ui/base/BUILD.gn, ui/base/accelerators/accelerator.cc, ui/base/base_window.h, ui/base/cocoa/secure_password_input.h, ui/base/cocoa/secure_password_input.mm, ui/base/dragdrop/drop_target_win.cc, ui/base/l10n/l10n_util.cc, ui/base/resource/resource_bundle.cc, ui/base/resource/resource_bundle_android.cc, ui/base/resource/resource_bundle_mac.mm and 27 more.

## networking
14 changed paths in 1 patch files (15260 patch bytes).

Paths: net/disk_cache/backend_unittest.cc, net/disk_cache/blockfile/backend_impl.cc, net/disk_cache/blockfile/backend_impl.h, net/disk_cache/blockfile/in_flight_backend_io.cc, net/disk_cache/memory/mem_backend_impl.cc, net/http/transport_security_state.cc, net/ssl/ssl_config.cc, net/test/embedded_test_server/embedded_test_server.cc, services/network/public/cpp/resource_response_info.h, services/service_manager/embedder/main.cc, services/ui/public/cpp/gpu/gpu.cc, services/ui/public/cpp/gpu/gpu.h and 2 more.

## media
62 changed paths in 1 patch files (766692 patch bytes).

Paths: gpu/config/gpu_switches.cc, gpu/config/gpu_switches.h, gpu/ipc/client/gpu_channel_host.h, gpu/ipc/service/gpu_channel.cc, gpu/ipc/service/gpu_channel.h, media/BUILD.gn, media/base/audio_decoder_config.cc, media/base/audio_decoder_config.h, media/base/container_names.cc, media/base/container_names.h, media/base/container_names_unittest.cc, media/base/decoder_buffer.h and 50 more.

## dependencies
94084 changed paths in 224 patch files (1762575582 patch bytes).

Paths: third_party/SPIRV-Tools/src/.clang-format, third_party/SPIRV-Tools/src/.gitignore, third_party/SPIRV-Tools/src/.travis.yml, third_party/SPIRV-Tools/src/CHANGES, third_party/SPIRV-Tools/src/CMakeLists.txt, third_party/SPIRV-Tools/src/LICENSE, third_party/SPIRV-Tools/src/README.md, third_party/SPIRV-Tools/src/external/CMakeLists.txt, third_party/SPIRV-Tools/src/include/spirv-tools/libspirv.h, third_party/SPIRV-Tools/src/include/spirv/GLSL.std.450.h, third_party/SPIRV-Tools/src/include/spirv/OpenCL.std.h, third_party/SPIRV-Tools/src/include/spirv/spirv.h and 94072 more.

## other
34 changed paths in 1 patch files (40275 patch bytes).

Paths: .gitattributes, .gitmodules, android_webview/BUILD.gn, apps/launcher.cc, base/base_paths_mac.mm, base/base_paths_posix.cc, base/base_paths_win.cc, base/files/file_util_posix.cc, base/mac/foundation_util.mm, base/memory/shared_memory_posix.cc, base/path_service.cc, base/process/process_win.cc and 22 more.
