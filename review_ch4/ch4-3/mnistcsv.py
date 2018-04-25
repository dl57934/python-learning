import struct
savepath = './mnist/'
def to_csv(filename,maxdata):
    dataFile = open(savepath+filename+'-images-idx3-ubyte','rb')
    lblFile = open(savepath+filename+'-labels-idx1-ubyte','rb')
    csvFile = open(savepath+filename+'.csv','w',encoding='utf-8')
    mag,lblCount = struct.unpack('>II',lblFile.read(8))
    mag,dataCount = struct.unpack(">II",dataFile.read(8))
    row, col = struct.unpack(">II",dataFile.read(8))
    print(row,col)
    pixels = row * col
    res = []
    for idx in range(lblCount):
        if idx > maxdata: break
        label = struct.unpack('B',lblFile.read(1))[0]
        data = dataFile.read(pixels)
        data = list(map(lambda n : str(n),data))
        csvFile.write(str(label)+',')
        csvFile.write(','.join(data)+'\n')


to_csv('train',5000)
to_csv('t10k',1000)




