[app]

title = NGL Spammer
package.name = nglspammer
package.domain = org.anonymousupikiller
source.dir = .
version = 1.0.0
requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 0

android.accept_sdk_license = True
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30
android.build_tools_version = 30.0.3
android.arch = arm64-v8a
android.permissions = INTERNET
