import requests

def main():

    result = requests.get("http://api.open-notify.org/astros.json")

    if result.status_code == 200:
        print('Result as JSON: {}\nResult as text: {}' .format(result.json(), result.text))
    else:
        print('Something went wrong.')


if __name__ == '__main__':
    main()