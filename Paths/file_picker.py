"""File picker logic."""
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import sys

GET_APK = 1
GET_SDK = 2
GET_CRAWL = 3


def get_path(target: int) -> str:
    """Open Tkinter window to navigate to .apk file.

    File path will be returned and used to crawl the android application for
    automatic testing purposes.
    """
    title = ""
    filename = ""
    directory = ""
    Tk().withdraw()  # stops extra GUI from appearing.

    if target == GET_APK:
        title = "Select APK file"
        filename = askopenfilename(title=title,
                                   filetypes=[("APK files", '*.apk')])
    elif target == GET_SDK:
        title = "Select SDK directory"
        directory = askdirectory(title=title)
    elif target == GET_CRAWL:
        title = "Select app-crawler directory"
        directory = askdirectory(title=title)
    else:
        print("Invalid option passed to get_path function. "
              "Target must be of type int.")
        sys.exit(2)

    if filename:
        return filename
    elif directory:
        return directory
    else:
        print("Did not pick a file. Exiting...")
        sys.exit(2)
