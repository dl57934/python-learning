import urllib.request as req
from bs4 import BeautifulSoup as bs

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

savename = "forecast.xml"

req.urlretrieve(url,savename)

xml = open(savename,"r",encoding = "utf-8").read()
soup = bs(xml,"html.parser")

info = {}

for location in soup.find_all("location"):
    city = location.find("city").string
    weather = location.find("wf").string
    if not (weather in info):
        info[weather] = []
    info[weather].append(city)


for wf in info.keys():
    print("+",wf)
    for city in info[wf]:
        print("-",city)
 
