import urllib.request

url = "http://www.earlyadopter.co.kr/wp-content/uploads/2017/09/Millennium-Falcon-1.jpg"

readData = urllib.request.urlopen(url).read()

savename = "milleniumPalcon.png"

with open(savename,"wb") as fb:
    fb.write(readData)
