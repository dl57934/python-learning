from urllib import request
from bs4 import BeautifulSoup
import requests

url ="https://namu.wiki/w/%EC%8A%A4%ED%8A%B8%EB%9D%BC%EC%9D%B4%ED%81%AC%20%ED%94%84%EB%A6%AC%EB%8D%A4%20%EA%B1%B4%EB%8B%B4?from=%EC%8A%A4%ED%8A%B8%EB%9D%BC%EC%9D%B4%ED%81%AC%20%ED%94%84%EB%A6%AC%EB%8D%A4"

data = requests.get(url)
data = data.text
soup = BeautifulSoup(data,'html.parser')
data = soup.select("""body > div.content-wrapper > article > div.wiki-content.clearfix > div > div""")[5].select('p')[0]
for data2 in data:
    print(data2.string)



