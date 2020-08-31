import requests

lat = 35.838837
lon = 128.623329
api_key = "f05209d74bc04ecc620d5c695eeb82c8"

url = "api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

res = requests.get(url)

print(res)