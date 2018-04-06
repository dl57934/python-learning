from urllib import parse
from urllib import request
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {'stnId':143}
params = parse.urlencode(values)
url = API + '?'+ params
print('url: '+url)
data = request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
#read안쓰면 어디서 반응이 왔는지 나오고
#read쓰면 바이트 값이 나온다