#!/usr/bin/env python
"""Runs an android app-crawler when given .apk directory.

Will use Google's automatic app-crawler that will test android apps by
interacting with all compponents present in the app and writes a log to
file.
"""
# Tells interpreter which version of python to use when calling this script.

# Had to run "chmod u+x app.py" command inside root folder to be able to run as
# global script
from Commands import cmd as cmd
from Paths import paths as paths
from Strings.help_file import help_message
from Paths import file_picker
from Paths.paths import CrawlPath
import getopt
import sys

crawlPath = CrawlPath()
settings = crawlPath.read_settings()
print(settings)

try:
    opts, args = getopt.getopt(sys.argv[1:], "hasc")   # unpacking tuple
    for opt, arg in opts:
        if opt == "-h":
            print(help_message)
        elif opt == "-a":
            apk_dir = file_picker.get_apk_path()
            # set a "last used path" that will be used if -a is not used
            settings["apk_dir"] = apk_dir
            crawlPath.save_settings(settings)
            # print("You chose:", apk_dir)
        elif opt == "-s":
            # get Android SDK path and store in an options file
            pass
        elif opt == "-c":
            # get App-Crawler directory and store it
            pass
        else:
            print("invalid argument.")
except getopt.GetoptError:
    print("Exception thrown whilslt parsing args")
    sys.exit(2)

"""
this = f"{cmd.JAVA} {paths.CRAWLER_DIR} {cmd.APK_FILE} (your .apk file dir)" \
    f"{cmd.ANDROID_SDK} {paths.SDK_DIR}"
"""
