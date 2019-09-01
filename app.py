#!/usr/bin/env python
# Tells interpreter which version of python to use when calling this script.

# Had to run "chmod u+x app.py" command inside root folder to be able to run as
# global script
from Commands import cmd as cmd
from Paths import paths as paths


this = f"{cmd.JAVA} {paths.CRAWLER_DIR} {cmd.APK_FILE} (your .apk file dir)" \
    f"{cmd.ANDROID_SDK} {paths.SDK_DIR}"

print(this)
