import requests

def main():

    result = requests.get("http://api.open-notify.org/astros.json")
    print(result.status_code)

if __name__ == '__main__':
    main()