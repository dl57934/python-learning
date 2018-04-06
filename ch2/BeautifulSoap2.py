from bs4 import BeautifulSoup
from urllib import request
from urllib import parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {'id':'108'}
params = parse.urlencode(values)
print("params: ",params)
url = API +"?"+params

data = request.urlopen(url)
soup = BeautifulSoup(data,"html.parser")

print(soup.find("title").string)
print(soup.find("wf").string)
