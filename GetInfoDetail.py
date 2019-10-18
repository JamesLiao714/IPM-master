# function [ cameraInfo, ipmInfo ] = GetInfoDetail(I)
# I = inputImage
# camera Info
class cameraInfo():
    def __init__(self):
        # focal length
        self.focalLengthX=1200.6831
        self.focalLengthY=1200.6831
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
class ipmInfo:
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

R = I(:,:,1)
[Rheight, Rwidth] =  size(R)
u = Rheight
v = Rwidth
vpp = GetVanishingPoint(cameraInfo)
vp.x = vpp(1)
vp.y = vpp(2)
uvLimitsp = [
            vp.x, ipmInfo.ipmRight,ipmInfo.ipmLeft, vp.x;
            ipmInfo.ipmTop, ipmInfo.ipmTop, ipmInfo.ipmTop,  ipmInfo.ipmBottom]

xyLimits = TransformImage2Ground(uvLimitsp,cameraInfo)
row1 = xyLimits(1,:)
row2 = xyLimits(2,:)
xfMin = min(row1); xfMax = max(row1)
yfMin = min(row2); yfMax = max(row2)

[outRow outCol] = size(outImage)
stepRow = (yfMax - yfMin)/outRow
stepCol = (xfMax - xfMin)/outCol
xyGrid = zeros(2,outRow*outCol)
y = yfMax-0.5*stepRow
for i = 1:outRow
    x = xfMin+0.5*stepCol
    for j = 1:outCol
        xyGrid(1,(i-1)*outCol+j) = x
        xyGrid(2,(i-1)*outCol+j) = y
        x = x + stepCol
    end
    y = y - stepRow
end
ipmInfo.xLimits(1) = xyGrid(1,1)
ipmInfo.xLimits(2) = xyGrid(1,end)
ipmInfo.yLimits(1) = xyGrid(2,end)
ipmInfo.yLimits(2) = xyGrid(2,1)
ipmInfo.xScale = 1/stepCol
ipmInfo.yScale = 1/stepRow
ipmInfo.width = outCol
ipmInfo.height = outRow
