"""Displays help options for commandline -h option.

This file contains the help message that will be displayed if the user
uses the -h commandline argument.
"""
help_message = """List of options:
    -a      Open filepicker to selelct .apk file and save filepath
    -c      Open filepicker to set app-crawler filepath
    -s      Open filepicker to set Android SDK filepath
    -r      Run app-crawler (optional). Can run the command right after picking
            a directory or file. e.g. \'crawl.py -a -r\' lets user pick APK
            file and then immediately run script after."""
