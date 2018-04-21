import urllib.request as req
from bs4 import BeautifulSoup
import json
import os.path 


url = "https://api.github.com/repositories"
savename = "github.json"

if not os.path.exists(savename):
    req.urlretrieve(url,savename)


items  =  json.load(open(savename,"r",encoding= "utf-8"))

for item in items:
    print(item["name"] +" - "+item["owner"]["login"])
