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
        d = data.json()['delay']
        for line in d:

            print()
            print(f'Nazwa przystanku: {line["headsign"]}')
            print(f'RouteID: {line["routeId"]}')
            if line["delayInSeconds"] > 0:
                minutes = line["delayInSeconds"] // 60
                seconds = line["delayInSeconds"] % 60
                formatted_delay = f'{minutes} min {seconds} s'
                print(f'Delay: {formatted_delay}')
            print(f'theoreticalTime: {line["theoreticalTime"]}')






if __name__ == '__main__':
    main()
#Warszawska
#Gdynia Dworzec Gł. PKP 02
#10022
#16:06
#3 min 10 s