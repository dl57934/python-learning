import urllib.request

url = "http://www.naver.com"

data = urllib.request.urlopen(url).read()
data = data.decode("utf-8")
print(data)
