import urllib.request
import urllib.parse


url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

value = {"stnId":108}
value = urllib.parse.urlencode(value)

url = url + "?"+value

data = urllib.request.urlopen(url).read()
print(data.decode("utf-8"))
