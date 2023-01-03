from urllib import request
import json
import  current


def update(url, version):
    code_name = "demo"
    extention = ".py"
    request.urlretrieve(f"{url}{code_name}-{version}{extention}", f"{code_name}-{version}{extention}")


def run_program():
    pass


def main():
    # request and download de info file
    url = 'https://raw.githubusercontent.com/Jubskleiton/auto-updater/main/versions/latest_version.py'
    request.urlretrieve(url, 'latest_version.json')

    # Open the JSON file
    with open('latest_version.json', 'r') as file:
        # Load the JSON data into a Python variable
        data = json.load(file)

    # Now you can access the data in the variable as a Python object
    if data["latest"] != current.CURRENT_VERSION:
        latest_version_splited = data["latest"].split(".")
        if int(latest_version_splited[0]) > current.CURRENT_VERSION_SPLITED[0]:
            print("Major update detected updating now")
            update(data["url"], data["latest"])
        elif int(latest_version_splited[1]) > current.CURRENT_VERSION_SPLITED[1]:
            print("New version detected updating")
            update(data["url"], data["latest"])
        elif int(latest_version_splited[2]) > current.CURRENT_VERSION_SPLITED[2]:
            update(data["url"], data["latest"])
    else:
        run_program()