import struct 

def to_csv(name,maxdata):
    savePath = "./trainImages/"
    lbl_f = open(savePath+name+"-labels-idx1-ubyte","rb")
    img_f = open(savePath+name+"-images-idx3-ubyte","rb")
    csv_f = open(savePath+name+".csv","w",encoding="utf-8")
    # 숫자 2개가 1바이트 
    mag, img_count = struct.unpack(">II",img_f.read(8))
    mag, lbl_count = struct.unpack(">II",lbl_f.read(8))
    rows, cols = struct.unpack(">II",img_f.read(8))
    pixels = rows *cols
    res = []
    for idx in range(lbl_count):
        if idx > maxdata: break
        label = struct.unpack("B",lbl_f.read(1))[0]
        # bdata는 바이트
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n),bdata))
        csv_f.write(str(label)+',')
        csv_f.write(",".join(sdata)+"\r\n")
        
    lbl_f.close()
    img_f.close()
    csv_f.close()
to_csv('train',30000)
to_csv('t10k',1000)
