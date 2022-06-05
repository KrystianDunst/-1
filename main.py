import requests
from pprint import pprint


def main():
    response = requests.get('http://api.zdiz.gdynia.pl/pt/stops')
    # pprint(response.json())

    filtered_stops = []
    for stop in response.json():
        if 'Warszawska' in stop['stopName']:
            filtered_stops.append(stop)

    # pprint(filtered_stops)
    delay_data = []
    for stop in filtered_stops:
        stop_id = stop['stopId']
        data = requests.get(f'http://api.zdiz.gdynia.pl/pt/delays?stopId={stop_id}')
        delay_data.extend(data.json()['delay'])

    pprint(delay_data)


if __name__ == '__main__':
    main()
