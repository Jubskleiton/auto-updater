from urllib import request

def main():
    url = 'https://raw.githubusercontent.com/Jubskleiton/auto-updater/main/versions/latest_version.py?token=GHSAT0AAAAAAB47M6BRJ2SWC2XPETOW4L2EY5UL2HQ'
    request.urlretrieve(url, 'latest_version.py')
