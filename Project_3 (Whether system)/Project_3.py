import requests

city_name = 'Islamabad'
API_Key = 'd24b2e7766ec335915cf2c131bd69302'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather is ', data['weather'][0]['description'])
    print('Current Temperature is ', data['main']['temp'])
    print('Current Temperature Feels like is ', data['main']['feels_like'])
    print('Humidity is ', data['main']['humidity'])
