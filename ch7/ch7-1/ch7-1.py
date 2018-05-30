import cv2
# def getMean():
#     img = cv2.imread('images/Ironman.PNG', cv2.IMREAD_GRAYSCALE)
#     img = cv2.resize(img, None, fx=16/702, fy=16/400, interpolation=cv2.INTER_AREA)
#     avg = img[:].mean()
#     diff = 1*(img > avg)
#     return diff
#
# def getAverageHash(MeanPixel):
#     bhash = []
#     for nl in MeanPixel:
#         sl = [str(i) for i in nl]
#         s2 = "".join(sl)
#         i = int(s2, 2)
#         bhash.append("%04x" %i)
#     return "".join(bhash)
#
# ahash = getMean()
# hashData= getAverageHash(ahash)
img = cv2.imread('../images/101/chair')
print(img.shape[0])






