import requests
def get_weather(text):
  api_key = '' # Input Your API Key Here
  city= text
  url=f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
  response = requests.get(url)
  data = response.json()

  if 'error' not in 'data':
    location = data['location']['name']
    temparature = data['current']['temp_c']
    humidity = data['current']['humidity']
    weather = data['current']['condition']['text']

    print(f'Location: {location}, ')
    print(f'Temperature: {temparature},')
    print(f'Humidity: {humidity},')
    print(f'Description: {weather}')
  else:
    print('city not found')


prompt = input('what city would you like to get the weather of? ')
get_weather(prompt)


