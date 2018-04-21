from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
session = requests.session()
loginInfo = {
   "loginId" : "dl57934@naver.com",
    "password" : "!dngmadl14"
}



url_login = "http://hoony-gunputer.tistory.com/manage"
res = session.post(url_login, data=loginInfo)
print(res.text)
url_myPage = "http://hoony-gunputer.tistory.com/manage"
res = session.get(url_myPage)
print(res.text)


