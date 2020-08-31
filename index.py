import requests

url = "http://api.openweathermap.org/data/2.5/weather"

params = {
  'lat':'35.838837',
  'lon':'128.623329',
  'appid':'f05209d74bc04ecc620d5c695eeb82c8'
}

res = requests.get(url, params=params).json()

print(res['weather'][0]['main'])
print(res['sys']['country'],res['name'])