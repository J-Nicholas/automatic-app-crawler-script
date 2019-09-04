"""Contains path constants to SDK directory and app crawler directory."""

import json
from pathlib import Path
from Paths import file_picker
from Paths.file_picker import get_path
from sys import exit


class CrawlPath:
    """Responsible for saving and loading json files and checking paths."""

    def __init__(self):
        """Initialise the settings path."""
        self.__folder_path = Path.home() / ".auto_crawl/"
        self.__settings_filename = "settings.json"
        self.__full_path = self.folder_path / self.settings_filename
        if not self.user_dir_exists():
            # make dir and settings file with default values
            print("Settings folder not found. Creating settings folder in...\n"
                  + self.__folder_path)
            self.make_dir()
        if not self.settings_exist():
            self.initial_setup()
            print("Creating settings file...")
            self.make_settings_file()

    @property
    def folder_path(self) -> str:
        """Get folder path directory."""
        return self.__folder_path

    @property
    def settings_filename(self):
        """Get name of settings file."""
        return self.__settings_filename

    @property
    def full_path(self) -> str:
        """Get absolute Path object for settings file."""
        return self.__full_path

    def user_dir_exists(self) -> bool:
        """Check if directory-settings file exists."""
        if self.folder_path.exists():
            return True
        else:
            return False

    def settings_exist(self) -> bool:
        """Check if a settings file is in folder path."""
        if self.full_path.exists():
            return True
        else:
            return False

    def make_dir(self):
        """Initalise settings folder with default settings file."""
        self.folder_path.mkdir()

    def make_settings_file(self) -> None:
        """Initalise settings file with default directories."""
        json_file = json.dumps(self.__default_settings)
        self.full_path.write_text(json_file)

    def read_settings(self):
        """Read directory settings file and return directory dictionary."""
        if not self.user_dir_exists():
            print("Can't read settings, folder hasn't been created yet.")
            return
        elif not self.settings_exist():
            print("Could not read settings, file does not exist yet.")
            return
        else:
            json_object = self.full_path.read_text()
            return json.loads(json_object)

    def save_settings(self, json_settings):
        """Save directory settings to file as JSON object."""
        json_object = json.dumps(json_settings)
        self.full_path.write_text(json_object)

    def initial_setup(self):
        """Ask user to locate filepaths required for application to run.

        Ask user to locate Android SDK path, app-crawler.jar, and the .apk file
        that they want the app-crawler to test.
        """
        print("Performing first time setup. Please locate the Android SDK "
              "folder, the APK file you wish to test using the app-crawler, "
              "and the App-crawler.jar file.")

        response = input("Are you ready? (y/n)").lower()
        if response == "y" or response == "yes":
            android_sdk = Path(get_path(file_picker.GET_SDK))
            print("Android SDK path selected:", android_sdk.absolute())

            android_apk = Path(get_path(file_picker.GET_APK))
            print("Android APK path selected:", android_apk.absolute())

            app_crawler = Path(get_path(file_picker.GET_CRAWL))
            print("App crawler path selected:", app_crawler.absolute())

            if not (android_apk.exists() or android_sdk.exists() or
                    app_crawler.exists()):
                print("Error whilst picking directories.")
                exit(4)
            self.__default_settings = dict(
                sdk_dir=android_sdk.resolve().as_posix(),
                apk_dir=android_apk.resolve().as_posix(),
                crawler_dir=app_crawler.resolve().as_posix())
        else:
            print("Exiting...")
            exit(0)
            pass
