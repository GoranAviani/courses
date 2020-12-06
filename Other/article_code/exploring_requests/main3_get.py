import requests

def main():

    result = requests.get("http://api.open-notify.org/astros.json")

    if result.status_code == 200:
        print('Success!')
    else:
        print('Something went wrong.')


if __name__ == '__main__':
    main()