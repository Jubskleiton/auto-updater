from urllib import request
import json

def main():
    url = 'https://raw.githubusercontent.com/Jubskleiton/auto-updater/main/versions/latest_version.py'
    request.urlretrieve(url, 'latest_version.json')

    # Open the JSON file
    with open('latest_version.json', 'r') as file:
        # Load the JSON data into a Python variable
        data = json.load(file)

    # Now you can access the data in the variable as a Python object
    print(data['latest'])