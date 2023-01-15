from urllib import request
import os
import json


if not os.path.exists("C://Program Files/Jubskleion"):
    os.mkdir("C://Program Files/Jubskleion")
if os.path.exists("C://Program Files/Jubskleion/Updater"):
    print("Folder C://Program Files/Jubskleion/Updater already exists !")
    while True:
        print("\nDo you want to reinstall the updater")
        reinstall = input("yes (y) or no (n) ? ")
        if reinstall == "y":
            break
        elif reinstall == "n":
            break
        else:
            print("use 'y' or 'n' to answer")
else:
    os.mkdir("C://Program Files/Jubskleion/Updater")
    url = 'https://raw.githubusercontent.com/Jubskleiton/auto-updater/main/versions/latest_version.json'
    request.urlretrieve(url, 'C://Program Files/Jubskleion/Updater/latest_version.json')
    with open('latest_version.json', 'r') as file:
        latest = json.load(file)
    print("downloading latest .exe file")
    request.urlretrieve(f"{latest['url']}{latest['program_name']}-{latest['version']}{latest['program_extention']}","{latest['program_name']}-{latest['version']}{latest['program_extention']}")
    print("updating current.json file")
    with open('current.json', 'w') as file:
        to_dump = {"CURRENT_VERSION": f"{latest['version']}", "CURRENT_VERSION_SPLITED": latest["version_splited"]}
        json.dump(to_dump, file)
    print("creating programs.json")
