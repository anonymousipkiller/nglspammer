[app]

title = NGL Spammer
package.name = nglspammer
package.domain = org.anonymousipkiller
source.dir = .

version = 1.0.0
version.code = 1

requirements = python3,kivy,requests

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0

fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 1

android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 23b
android.sdk = 33

android.gradle_dependencies =

android.add_src =

android.permissions = INTERNET

android.arch = arm64-v8a
