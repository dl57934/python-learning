from bs4 import BeautifulSoup as bs
import urllib.request as req
import json

url = "https://api.github.com/repositories"
saveName = "example.json"
req.urlretrieve(url,saveName)

datas = json.load(open(saveName,"r",encoding="utf-8"))

for data in datas:
    print(data["id"],data["name"])
