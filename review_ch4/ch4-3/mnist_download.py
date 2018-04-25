import urllib.request as req
import gzip, os, os.path

savepath = './mnist/'
baseUrl = "http://yann.lecun.com/exdb/mnist/"

def downloadDataFile(filename):
    dataName = filename + "-images-idx3-ubyte.gz"
    dataLabel = filename + "-labels-idx1-ubyte.gz" 
    locdataName = savepath+dataName
    loclabelName = savepath +dataLabel
    if not os.path.exists(savepath):os.mkdir(savepath)
    if not os.path.exists(locdataName and loclabelName): 
        req.urlretrieve(baseUrl+dataName,locdataName)
        req.urlretrieve(baseUrl+dataLabel,loclabelName)
    openGzip(filename)

def openGzip(filename):
    data = []
    locdataName = savepath+filename + "-images-idx3-ubyte.gz" 
    loclabel = savepath + filename + "-labels-idx1-ubyte.gz" 
    data.append(locdataName)
    data.append(loclabel)
    for fName in data:
        with gzip.open(fName,'rb') as fp :
            body = fp.read()
            rawdataName = fName.replace('.gz','')
            with open(rawdataName,'wb') as f:
                f.write(body)

downloadDataFile('t10k')
downloadDataFile('train')
