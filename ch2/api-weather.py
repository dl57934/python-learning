import requests 
import json

apiKey= "a6c578487d31e2eb09e372b7fe494ad3"

cities = ["Seoul,KR","Tokyo,JP","New York,US"]

api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

for name in cities:
    url = api.format(city=name, key=apiKey)
    r= requests.get(url)
    data = json.loads(r.text)
    print("+ 도시 =",data["name"])
    print("| 날씨 =",data["weather"][0]["description"])
