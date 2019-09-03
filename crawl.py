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

try:
    opts, args = getopt.getopt(sys.argv[1:], "hascr")   # unpacking tuple
    for opt, arg in opts:
        if opt == "-h":
            print(help_message)

        elif opt == "-a":
            continue
            apk_dir = file_picker.get_path(file_picker.GET_APK)
            # set a "last used path" that will be used if -a is not used
            settings["apk_dir"] = apk_dir
            crawlPath.save_settings(settings)

        elif opt == "-s":
            # TODO: get Android SDK path and store in an options file
            sdk_dir = file_picker.get_path(file_picker.GET_SDK)
            settings["sdk_dir"] = sdk_dir
            crawlPath.save_settings(settings)

        elif opt == "-c":
            # TODO: get App-Crawler directory and store it
            crawler_dir = file_picker.get_path(file_picker.GET_CRAWL)
            settings["crawler_dir"] = crawler_dir
            crawlPath.save_settings(settings)
        elif opt == "-r":
            if len(opts) > 1:
                if opts[len(opts)-1][0] == "-r":
                    # if r is the last argument
                    print("RUN")
                else:
                    sys.exit("-r must come last.")
        else:
            print("invalid argument.")



    if len(opts) == 0:
        # check if APK has been saved before
        if settings.get("apk_dir", "") is not "":
            print("Using last used APK file path. Run this command "
                  "with -a argument to choose new APK.")
            # TODO: run crawler command in terminal
            pass
        else:
            print("APK filepath not on record. Run this command with -a to "
                  "select APK and save its filepath.")
except getopt.GetoptError:
    print("Exception thrown whilslt parsing args")
    sys.exit(2)

"""
this = f"{cmd.JAVA} {paths.CRAWLER_DIR} {cmd.APK_FILE} (your .apk file dir)" \
    f"{cmd.ANDROID_SDK} {paths.SDK_DIR}"
"""
