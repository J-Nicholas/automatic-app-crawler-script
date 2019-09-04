# Readme
This is a simple python script that I wrote for Linux operating systems to make using Google's Android [App-Crawler](https://developer.android.com/training/testing/crawler) simpler to use. The regular way involves writing long directory paths in the terminal with various commands. This script saves the directories in a settings file in *~Home/.app_crawler*. 

## Usage
1. Run `git clone https://github.com/J-Nicholas/automatic-app-crawler-script.git <Desired Folder Location>`

1. Run `vim ~/.profile` command to open .profile file. (or any text editor you wish). 

1. Add  `export PATH="<Desired Folder Location>:$PATH"` to its own line so that you can run the python script from any folder in the terminal.

1. To allow the script to be executed, navigate to the root of your desired folder location and run `chmod u+x crawl.py` from the terminal.

Now, you can run `crawl.py` from any directory and the script will run. The first time the script runs; a first time setup will occur and a filepicker will allow you to quickly navigate to each of the required components, namely the Android SDK folder, thte APK file that you wish to test and the locataion of the app-crawler.jar. These directories will then be saved to the settings file in */home/.auto_crawl/* 

## Requirements
You need to have the following to use this script:
* Google's App-Crawler [Download](https://dl.google.com/appcrawler/beta1/app-crawler.zip)
* Android Emulator (Included with Android Studio)
* Android SDK (Included with Android Studio)
* Compiled Android .apk file 

Note that the emulator needs to be running in order to work.
