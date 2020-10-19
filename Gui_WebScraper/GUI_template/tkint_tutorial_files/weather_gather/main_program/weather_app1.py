from weather_source import *
from weather_data import *
from colors import *

# Screen Size Data
HEIGHT = 800
WIDTH = 800


# IMPORTED DATA FROM WEATHER_DATA
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        max_temp = weather['main']['temp_max']
        min_temp = weather['main']['temp_min']
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']

        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s\nMax Temperature (°F): %s' \
                    '\nMin Temperature (°F): %s \nHumidity: %s \nWind Speed: %s' % (name, desc, temp,max_temp,
                                                                                    min_temp,humidity,wind_speed)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = '3d7102c18ab158257bce2ab1be33d4df'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


# Root
root = Tk()

# Screen Size
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Application Background
background_image = PhotoImage(file='../images/background/wallhaven-r2eg1w.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# API Key from home.openweathermap.org
# https://openweathermap.org/forecast5
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# 3d7102c18ab158257bce2ab1be33d4df


# To organize widgets use Frame , bd = border
frame = Frame(root, bg='#99b3ff', bd=5)

frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Button Functionaliy
# command -> runs x,y,z commands

button = Button(frame, text='Get Weather!', font=40, command=lambda: get_weather(entry.get()))

button.place(relx=.7, relheight=1, relwidth=0.3)

# User Typing Enabled
entry = Entry(frame, font=('Roboto',25) )
entry.place(relwidth=.65, relheight=1)

lower_frame = Frame(root, bg='#99b3ff', bd=10)
lower_frame.place(relx=.5, rely=.25, relwidth=.75, relheight=.6, anchor='n')

label = Label(lower_frame, font=('Roboto',20) )
label.place(relwidth=1, relheight=1)

root.mainloop()
