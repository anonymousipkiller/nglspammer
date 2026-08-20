[app]

title = NGL Spammer
package.name = nglspammer
package.domain = org.anonymouspickiller
source.dir = .
version = 1.0.0
requirements = python3,kivy==2.3.0,cython==0.29.33

orientation = portrait
fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 0

android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.build_tools = 33.0.2
android.archs = arm64-v8a
android.permissions = INTERNET
