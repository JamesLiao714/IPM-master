#function [ cameraInfo, ipmInfo ] = GetInfo
# camera Info
class CameraInfo():
    def __init__(self):
        # focal length
        self.focalLengthX=600
        self.focalLengthY=600
        # optical center
        self.opticalCenterX=638.1608
        self.opticalCenterY=738.8648
        # height of the camera in mm
        self.cameraHeight=1879.8
        # 393.7 + 1786.1
        # pitch of the camera
        self.pitch=15.5
        # yaw of the camera
        self.yaw=0.0
        # imag width and height
        self.imageWidth=1280
        self.imageHeight=1024

# ipmInfo
# settings for stop line perceptor
class IpmInfo:
    def __init__(self):
        #128
        self.ipmWidth = 640
        #160#320#160 
        #96
        self.ipmHeight = 480
        #120#240#120
        self.ipmLeft = 256
        #80 #90 #115 #140 #50 #85 #100 #85
        self.ipmRight = 1024
        #500 #530 #500 #590 #550
        self.ipmTop = 500
        #220 #200 #50
        self.ipmBottom = 1000
        #360 #350 #380
        #0 bilinear, 1: NN
        self.ipmInterpolation = 0
        self.ipmVpPortion = 0
        #.09 #0.06 #.05 #.125 #.2 #.15 #.075#0.1 #.05

def GetInfo():
    return CameraInfo(), IpmInfo()

