import os.path, gzip, os
import urllib.request as req
filename = ["train-images-idx3-ubyte.gz","train-labels-idx1-ubyte.gz","t10k-images-idx3-ubyte.gz","t10k-labels-idx1-ubyte.gz"]

baseurl = 'http://yann.lecun.com/exdb/mnist/'

savepath= './trainImages'
if not os.path.exists(savepath): os.mkdir(savepath)
for f in filename:
    url = baseurl + f
    loc = savepath+'/'+f
    if not os.path.exists(loc): 
        req.urlentrieve(url,loc)

for f in filename:
    savefile = f.replace(".gz","")
    with gzip.open(savepath+'/'+f,'rb') as fp:
        body = fp.read()
        with open(savepath+"/"+savefile,'wb') as w:
             w.write(body)
