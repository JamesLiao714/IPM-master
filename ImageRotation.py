import cv2

class Info(object):
    def __init__(self, dct):
        self.dct = dct

    def __getattr__(self, name):
        return self.dct[name]

pic = 27
image = cv2.imread('../road5/'+str(pic)+'.jpg')
height = int(image.shape[0]) # row y
width = int(image.shape[1]) # col x
cameraInfo = Info({
    "focalLengthX": 4600, # 1200.6831,         # focal length x
    "focalLengthY": 3400, # 1200.6831,         # focal length y
    "opticalCenterX": int(width / 2), # 638.1608,        # optical center x
    "opticalCenterY": int(height / 2), # 738.8648,       # optical center y
    "cameraHeight": 1500, # 1879.8,  # camera height in `mm`
    "pitch": 7,           # rotation degree around x
    "yaw": 0,              # rotation degree around y
    "roll": 1.5              # rotation degree around z
})

M = cv2.getRotationMatrix2D(
    (cameraInfo.opticalCenterX, cameraInfo.opticalCenterY), cameraInfo.roll, 1)
image = cv2.warpAffine(image, M, (width, height))
cv2.imwrite('../road5/'+str(pic)+'_rotate.jpg',image)