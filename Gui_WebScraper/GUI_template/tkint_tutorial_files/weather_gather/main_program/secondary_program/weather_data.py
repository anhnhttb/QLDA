from weather_source import *
from colors import *


def format_response(weather_response):
    name = weather_response['name']
    description = 'You\'ve searched for: ', bold, red, weather_response['name'], end
    # get the first entry & the 'description' as listed in the terminal after print(response.json()) was active
    temp = 'It\'s currently', red, weather_response['weather'][0]['description'], end, ' at this time.'
    return str(name) + ' ' + str(description) + ' ' + str(temp)


def get_weather(city):
    weather_key = '3d7102c18ab158257bce2ab1be33d4df'
    # url = 'https://api.openweathermap.org/data/2.5/forecast'
    # weather = current
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather_response = response.json()

    # print(response.json())
    print('You\'ve searched for: ', bold, red, weather_response['name'], end)
    # get the first entry & the 'description' as listed in the terminal after print(response.json()) was active
    print('It\'s currently', red, weather_response['weather'][0]['description'], end, ' at this time.')

    # Temperature Color change, if its >= 70 -> red , else its blue
    if weather_response['main']['temp'] >= 70:
        print('Temperature: ', red, weather_response['main']['temp'], '°F', end)
    elif weather_response['main']['temp'] >= 55:
        print('Temperature: ', yellow, weather_response['main']['temp'], '°F', end)
    else:
        print('Temperature: ', blue, weather_response['main']['temp'], '°F', end)
    # MAX TEMP
    if weather_response['main']['temp_max'] >= 70:
        print('Max Temperature: ', red, weather_response['main']['temp_max'], '°F', end)
    elif weather_response['main']['temp_max'] >= 55:
        print('Max Temperature: ', yellow, weather_response['main']['temp_max'], '°F', end)
    else:
        print('Max Temperature: ', blue, weather_response['main']['temp_max'], '°F', end)

    # MIN TEMP
    if weather_response['main']['temp_min'] >= 70:
        print('Min Temperature: ', red, weather_response['main']['temp_min'], '°F', end)
    elif weather_response['main']['temp_min'] >= 55:
        print('Min Temperature: ', yellow, weather_response['main']['temp_min'], '°F', end)
    else:
        print('Min Temperature: ', blue, weather_response['main']['temp_min'], '°F', end)

    # HUMIDITY
    print('Humidity: ', cyan, weather_response['main']['humidity'], '%', end)

    # WIND SPEED
    print('Wind Speed: ', purple, weather_response['wind']['speed'], ' Mph', end)
