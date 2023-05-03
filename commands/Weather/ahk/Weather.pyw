import requests

api_key = 'a7fcd5f1-3270-4acc-849a-bd176ae68b62' #Ключ яндекс-api
lat, lon = '51.681804', '39.253333' # координаты Воронежа

url = f'https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&lang=ru_RU'
headers = {'X-Yandex-API-Key': api_key}

response = requests.get(url, headers=headers)

import pyttsx3

engine = pyttsx3.init()

weather_data = response.json()

temp = weather_data['fact']['temp']
feels_like = weather_data['fact']['feels_like']

text = f"Сейчас в Воронеже {temp} градусов, ощущается как {feels_like} градусов"
engine.say(text)
engine.runAndWait()

