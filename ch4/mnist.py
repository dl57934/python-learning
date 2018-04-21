import struct 

def load_csv(fname,maxdata):
    img_name = "./trainImages/"+fname + "-images-idx3-ubyte"
    lable_name = "./trainImages/"+fname +"-labels-idx1-ubyte"
    img_file = open(img_name,'rb')
    lable_file = open(lable_name,'rb')
    csvf_file = open("./trainImages/"+fname+".csv",'w',encoding = 'utf-8')
    mag, img_length = struct.unpack(">II",img_file.read(8))
    mag, lable_length = struct.unpack(">II",lable_file.read(8))
    rows, cols = struct.unpack(">II",img_file.read(8))
    pixels = rows * cols
    for idx in range(img_length):
        if idx > maxdata : break
        label = struct.unpack("B",lable_file.read(1))[0]
        bdata = img_file.read(pixels)
        sdata = list (map(lambda a :str(a),bdata))
        csvf_file.write(str(label)+',')
        csvf_file.write(','.join(sdata)+"\r\n")
    lable_file.close()
    img_file.close()
    csvf_file.close()




load_csv('t10k',3000)
load_csv('train',500)
