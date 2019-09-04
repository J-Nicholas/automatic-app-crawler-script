#!/usr/bin/env python
"""Runs an android app-crawler when given .apk directory.

Will use Google's automatic app-crawler that will test android apps by
interacting with all compponents present in the app and writes a log to
file.
"""
# Tells interpreter which version of python to use when calling this script.

# Had to run "chmod u+x app.py" command inside root folder to be able to run as
# global script
from Paths import paths as paths
from Strings.help_file import help_message
from Paths import file_picker
from Paths.paths import CrawlPath
from subprocess import call
from pathlib import Path
import getopt
import sys

crawlPath = CrawlPath()
settings = crawlPath.read_settings()    # dictionary
opts, args = "", ""

# TODO Prompt to ask user if their android emulator is running

# TODO catch correct exception if emulator was not active.


def run_app_crawler():
    """Run the terminal command to start app-crawler."""
    sdk_dir = settings["sdk_dir"]
    apk_dir = settings["apk_dir"]
    crawler_dir = settings["crawler_dir"]
    for key, path in settings.items():
        check_path = Path(path)
        if not check_path.absolute().exists():
            print(key + " " + path +
                  " mighth not exist. Run relevant command "
                  "to set its directory and ensure it is an absolute path. "
                  "i.e. does not start with \'~\'.\n" +
                  help_message)
            sys.exit(5)

    call(["java", "-jar", crawler_dir, "--apk-file",
         apk_dir, "--android-sdk", sdk_dir])


try:
    opts, args = getopt.getopt(sys.argv[1:], "hascr")   # unpacking tuple

except getopt.GetoptError:
    print("Exception thrown whilslt parsing args")
    sys.exit(1)

for opt, arg in opts:
    if opt == "-h":
        print(help_message)

    elif opt == "-a":
        apk_dir = file_picker.get_path(file_picker.GET_APK)
        # Set a "last used path" that will be used if -a is not used and save
        settings["apk_dir"] = apk_dir
        crawlPath.save_settings(settings)

    elif opt == "-s":
        # Get Android SDK path and store in an options file
        sdk_dir = file_picker.get_path(file_picker.GET_SDK)
        settings["sdk_dir"] = sdk_dir
        crawlPath.save_settings(settings)

    elif opt == "-c":
        # Get App-Crawler directory and store it
        crawler_dir = file_picker.get_path(file_picker.GET_CRAWL)
        settings["crawler_dir"] = crawler_dir
        crawlPath.save_settings(settings)

    elif opt == "-r":
        if len(opts) > 1:
            if opts[len(opts)-1][0] == "-r":
                # if r is the last argument
                run_app_crawler()
            else:
                sys.exit("-r must come last.")
        else:
            # if -r was input alone, do nothing
            pass
    else:
        print("invalid argument.")
        print(help_message)
        sys.exit(3)

# check if APK has been saved before
if settings.get("apk_dir", "") is not "":
    print("Using last used APK file path. Run this command "
          "with -a argument to choose new APK.")
    run_app_crawler()
else:
    print("APK filepath not on record. Run this command with -a to "
          "select APK and save its filepath.")
    sys.exit(4)
