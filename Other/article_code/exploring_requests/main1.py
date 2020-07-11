import requests

def main():
    ASTRONAUTS_IN_SPACE_URL = "http://api.open-notify.org/astros.json"

    result = requests.get(ASTRONAUTS_IN_SPACE_URL)



if __name__ == '__main__':
    main()