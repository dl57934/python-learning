import urllib.request as req
import gzip, os ,os.path

filename = ["train-images-idx3-ubyte.gz","train-labels-idx1-ubyte.gz","t10k-images-idx3-ubyte.gz","t10k-labels-idx1-ubyte.gz"]

storageLocation = "./trainImages"

if not os.path.exists(storageLocation): os.mkdir(storageLocation)
baseUrl = "http://yann.lecun.com/exdb/mnist"
for f in filename:
    if not os.path.exists(storageLocation+f):
        req.urlretrieve(baseUrl+"/"+f,storageLocation+"/"+f)

for f in filename:
    gfile = storageLocation +"/"+ f
    fFile = storageLocation+"/"+f.replace(".gz","")
    with gzip.open(gfile,"rb") as fp:
        body = fp.read()
        with open(fFile,"wb") as w:
            w.write(body)

        
        
