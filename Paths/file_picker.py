"""File picker logic."""
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import sys


def get_apk_path():
    """Open Tkinter window to navigate to .apk file.

    File path will be returned and used to crawl the android application for
    automatic testing purposes.
    """
    Tk().withdraw()  # stops extra GUI from appearing.
    filename = askopenfilename(title="Select APK file",
                               filetypes=[("APK files", '*.apk')])

    if filename:
        return filename
    else:
        print("Did not pick a file. Exiting...")
        sys.exit(2)
