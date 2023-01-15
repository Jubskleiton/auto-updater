# Programs Updater
> Code that auto updates programs.

## How to use it for your projects

In the 
[source/programs.json](https://github.com/Jubskleiton/auto-updater/blob/main/source/programs.json) add the information needed, create a repository with the 
[latest_version.jason](https://github.com/Jubskleiton/auto-updater/blob/main/versions/latest_version.json) containing the information needed.
The information needed is on the readme.md files on the folder os the respective fies

## The Project
This script is designed to check the latest version of a program and update it if a newer version is available. It uses the information provided in a JSON file to check the version of the program and update it. The JSON file should contain the following information:
> url: The URL of the location where the information about the latest version of the program is stored.

> program_name: The name of the program.

> path: The path where the program is stored on the user's local machine.

The verify_version function is used to check if a newer version of the program is available. It does this by downloading the latest version information from the specified URL and comparing it to the information about the current version of the program. If a newer version is available, the update function is called to download the latest version of the program and update the information about the current version in the JSON file.

The main function is where the script starts its execution. It loads the information from the 'programs.json' file, and for each program it calls the verify_version function. If it needs to be updated, it will call update function to download the new version of the program and update the current version information in the JSON file. If not up-to-date, the script will print that the program is up-to-date.

## Meta

[https://github.com/Jubskleiton](https://github.com/Jubskleiton)
