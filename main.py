import requests
from pprint import pprint


def main():
    response = requests.get('http://api.zdiz.gdynia.pl/pt/stops')
    # pprint(response.json())

    filtered_stops = []
    for stop in response.json():
        if 'Warszawska' in stop['stopName']:
            filtered_stops.append(stop)

    pprint(filtered_stops)


if __name__ == '__main__':
    main()
