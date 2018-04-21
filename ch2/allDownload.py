from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

processed_file = {
}

def enum_links(html, base):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select("link[rel='stylesheet']")
    links += soup.select('a[href]')
    results = []
    for a in links:
        href = a.attrs['href']
        url = urljoin(base,href)
        results.append(url)
    return results

def download_file(url):
    o = urlparse(url)
    savepath = './allDownloadResult/'+o.netloc+o.path
    print("savepath:",savepath,"netioc:",o.netloc,"o.path:",o.path)
    if re.search(r"/$",savepath): #폴더라면 index.html
        savepath+= "index.html"
    savedir = os.path.dirname(savepath)
    if os.path.exists(savepath): return savepath
    if not os.path.exists(savedir):
        makedirs(savedir)
    try:
        urlretrieve(url, savepath)
        time.sleep(1)
        return savepath
    except:
        print("다운 실패",url)
        return None

def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath is processed_file: return
    processed_file[savepath] = True
    html = open(savepath,"r",encoding="utf-8").read()
    links = enum_links(html, url)

    for link_url in links:
        if link_url.find(root_url) !=0 :
            if not re.search(r".css$",link_url):continue
        if re.search(r".(html|htm)$",link_url):
                analyze_html(link_url, root_url)
                continue
        download_file(link_url)

if __name__ == "__main__":
    url = "https://www.naver.com/"
    analyze_html(url,url)