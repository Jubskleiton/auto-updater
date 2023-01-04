from urllib import request
import json
import subprocess

CODE_NAME = "demo"
EXTENTION = ".exe"


def update(url, version):
  print("Baixando arquivo .exe atualizado")
  request.urlretrieve(f"{url}{CODE_NAME}-{version}{EXTENTION}", f"{CODE_NAME}-{version}{EXTENTION}")
  print("atualizando o arquivo current.json")
  with open('current.json', 'w') as file:
    # Load the JSON data into a Python variable
    cur_ver_spl = version.split(".")
    to_dump = {"CURRENT_VERSION" : f"{version}", "CURRENT_VERSION_SPLITED" : [int(cur_ver_spl[0]),int(cur_ver_spl[1]),int(cur_ver_spl[2])]}
    json.dump(to_dump, file)


def run_program(version):
    process = subprocess.Popen(f"{CODE_NAME}-{version}{EXTENTION}")

def main():
    # request and download de info file
    url = 'https://raw.githubusercontent.com/Jubskleiton/auto-updater/main/versions/latest_version.json'
    request.urlretrieve(url, 'latest_version.json')

    # Open the JSON file
    with open('latest_version.json', 'r') as file:
        # Load the JSON data into a Python variable
        data = json.load(file)
        # Open the JSON file
    with open('current.json', 'r') as file:
        # Load the JSON data into a Python variable
        current = json.load(file)

    # Now you can access the data in the variable as a Python object
    if data["latest"] != current["CURRENT_VERSION"]:
        latest_version_splited = data["latest"].split(".")
        if int(latest_version_splited[0]) > current["CURRENT_VERSION_SPLITED"][0]:
            print("Major update detected updating now")
            update(data["url"], data["latest"])
        elif int(latest_version_splited[1]) > current["CURRENT_VERSION_SPLITED"][1]:
            print("New version detected updating")
            update(data["url"], data["latest"])
        elif int(latest_version_splited[2]) > current["CURRENT_VERSION_SPLITED"][2]:
            update(data["url"], data["latest"])
    else:
        run_program(current["CURRENT_VERSION"])


if __name__ == '__main__':
    main()