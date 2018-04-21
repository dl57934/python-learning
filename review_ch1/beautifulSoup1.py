from bs4 import BeautifulSoup
import urllib.request



def what_event(urlInfo):
    url ="http://sports.news.naver.com/"+urlInfo+"/index.nhn"
    baseUrl = "http://sports.news.naver.com"
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data,"html.parser")
    data = soup.select("ul.home_news_list > li > a")
    for aData in data:
        href = aData.attrs['href']
        title = aData.attrs['title']
        print('기사제목: ',title,'기사주소: ',baseUrl + href)

event = input()
what_event(event)

