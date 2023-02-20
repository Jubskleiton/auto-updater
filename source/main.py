from urllib import request
import json


def verify_version(url: str, program_name: str, program_path: str):

    download_handler(url, program_name)

    # Open the JSON file
    with open(f"programs_info/{program_name}_latest.json", 'r') as file:
        # Load the JSON data into a Python variable
        latest = json.load(file)
        # Open the JSON file
    try:
        with open(f"programs_info/{program_name}.json", 'r') as file:
            # Load the JSON data into a Python variable
            current = json.load(file)
    except FileNotFoundError:
        print(f"Erro: {program_name}.json file not found, Raparing")
        with open(f"programs_info/{program_name}.json", 'w') as file:
            to_dump = {"version": "0.0.0", "version_splited": [0, 0, 0], "path" : program_path}
            json.dump(to_dump, file)
        return True
    except Exception as ex:
        print("ERROR!!")
        print(ex)
    return latest["version_splited"][0] > current["version_splited"][0] or latest["version_splited"][1] > current["version_splited"][1] or latest["version_splited"][2] > current["version_splited"][2]


def update(program_dict: dict):
    with open(f"programs_info/{program_dict['program_name']}_latest.json", 'r') as file:
        latest = json.load(file)
    print("Downloading newest .exe file")
    print(f"{latest['url']}{latest['program_name']}-{latest['version']}{latest['program_extention']}")
    request.urlretrieve(f"{latest['url']}{latest['program_name']}-{latest['version']}{latest['program_extention']}", f"{program_dict['path']}{latest['program_name']}-{latest['version']}{latest['program_extention']}")
    print("updating current.json file")
    with open(f"programs_info/{program_dict['program_name']}.json", 'w') as file:
        to_dump = {"version" : f"{latest['version']}", "version_splited" : latest["version_splited"]}
        json.dump(to_dump, file)


def download_handler(url, program_name):
    try:
        # request and download info file
        request.urlretrieve(url, f"programs_info/{program_name}_latest.json")
    except Exception as ex:
        print("can't download {program_name}_latest.json")
        print(f"ERROR: {ex}")
        quit()

#updates
def main():
    try:
        with open('programs.json', 'r') as file:
            # Load the JSON data into a Python variable
            programs = json.load(file)
    except FileNotFoundError:
        print("couldn't open programs.json, file doesn't exists.")
        print("creating default one")
        with open('programs.json', 'w') as file:
            to_dump = {"programs_urls_and_paths" : [{"url" : "https://raw.githubusercontent.com/Jubskleiton/auto-updater/main/versions/latest_version.json", "path" : "C://Program Files/Jubskleiton/Updater/", "program_name" : "jubskleiton_updater", "program_extention" : ".exe"}]}
            json.dump(to_dump, file)
    except Exception as ex:
        print("ERROR!!")
        print(ex)
        quit()
    for program in programs["programs_urls_and_paths"]:
        print("\n" + program["program_name"])
        if verify_version(program["url"], program["program_name"], program["path"]):
            update(program)
        else:
            print(f"{program['program_name']} up to date.")


if __name__ == '__main__':
    main()