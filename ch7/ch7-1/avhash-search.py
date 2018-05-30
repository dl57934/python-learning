import cv2
import numpy as np
import os, re

search_dir = "../images/101"
cache_dir = "../images/cache_avash"

if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)


def average_hash(fname):
    fname2 = fname[len(search_dir):]
    cache_file = cache_dir + "/" + fname2.replace('/', '_')+ ".csv"
    if not os.path.exists(cache_file):
        img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, None, fx=16 / img.shape[1], fy=16 / img.shape[0], interpolation=cv2.INTER_AREA)
        value = img[:]
        avg = value.mean()
        px = 1 * (value > avg)
    else:
        px = np.loadtxt(cache_file, delimiter=",")
    return px


def hamming_dist(a, b):
    aa = a.reshape(1, -1)
    ab = b.reshape(1, -1)
    dist = (aa != ab).sum()
    return dist


def enum_all_files(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            fname = os.path.join(root, f)
            if re.search(r'\.(jpg|jpeg|png)$', fname):
                yield fname


def find_image(fname, rate):
    src = average_hash(fname)
    for fname in enum_all_files(search_dir):
        dst = average_hash(fname)
        diff_r = hamming_dist(src, dst) / 256
        if diff_r < rate:
            yield (diff_r, fname)


srcfile = search_dir + "/chair/image_0016.jpg"
html = ""

sim = list(find_image(srcfile, 0.25))
sim = sorted(sim, key=lambda x: x[0])
for r, f, in sim:
    print(r, ">", f)
    s = '<div style="float:left;"><h3>[차이:' + str(r) + '-' + \
        os.path.basename(f) + ']</h3>' + \
        '<p><a href="' + f + '"><img src="' + f + '"width=400>' + \
        '</a></p></div>'
    html += s

html = """<html><head><meta charset="utf8"></head>
<body><h3>원래 이미지</h3><p>
<img src='{0}' width=400></p>{1}
</body></html>""".format(srcfile, html)

with open("./avhash-search-output.html", "w", encoding="utf-8") as f:
    f.write(html)
