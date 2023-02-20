from urllib import request
import os
import json

def download_handler(url, path):
    try:
        # request and download info file
        request.urlretrieve(url, path)
    except Exception as ex:
        print(f"download error")
        print(f"ERROR: {ex}")
        quit()

def do_it():
    if not os.path.exists("C://Program Files/Jubskleiton/Updater/programs_info"):
        os.mkdir("C://Program Files/Jubskleiton/Updater/programs_info")
    url = 'https://raw.githubusercontent.com/Jubskleiton/auto-updater/main/versions/latest_version.json'
    download_handler(url, 'C://Program Files/Jubskleiton/Updater/programs_info/jubskleiton_updater_latest.json')
    with open('C://Program Files/Jubskleiton/Updater/programs_info/jubskleiton_updater_latest.json', 'r') as file:
        latest = json.load(file)
    print("downloading latest .exe file")
    download_handler(f"{latest['url']}{latest['program_name']}-{latest['version']}{latest['program_extention']}", f"C://Program Files/Jubskleiton/Updater/{latest['program_name']}-{latest['version']}{latest['program_extention']}")
    print("creating jubskleiton_updater.json file")
    with open('C://Program Files/Jubskleiton/Updater/programs_info/jubskleiton_updater.json', 'w') as file:
        to_dump = {"version": f"{latest['version']}", "version_splited": latest["version_splited"], "path": "c:/programs/Jubskleiton/Updater/"}
        json.dump(to_dump, file)
    print("creating programs.json")
    with open('C://Program Files/Jubskleiton/Updater/programs.json', 'w') as file:
        to_dump = {"programs_urls_and_paths" : [{"url" : "https://raw.githubusercontent.com/Jubskleiton/auto-updater/main/versions/latest_version.json", "path" : "C://Program Files/Jubskleiton/Updater/", "program_name" : "jubskleiton_updater", "program_extention" : ".exe"}]}
        json.dump(to_dump, file)
    print("Updater Installed to the following path: C://Program Files/Jubskleiton/Updater/")
    return 0


if not os.path.exists("C://Program Files/Jubskleiton"):
    os.mkdir("C://Program Files/Jubskleiton")
if os.path.exists("C://Program Files/Jubskleiton/Updater"):
    print("Folder C://Program Files/Jubskleiton/Updater already exists !")
    while True:
        print("\nDo you want to reinstall the updater")
        reinstall = input("yes (y) or no (n) ? ")
        if reinstall == "y":
            do_it()
            break
        elif reinstall == "n":
            print("OK, Quiting")
            quit()
        else:
            print("use 'y' or 'n' to answer")
else:
    os.mkdir("C://Program Files/Jubskleiton/Updater")
    do_it()
