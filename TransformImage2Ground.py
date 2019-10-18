# function [ xyLimits ] = TransformImage2Ground( uvLimits,cameraInfo )
import numpy as np
from math import sin, cos, pi
def TransformImage2Ground(uvLimits, cameraInfo):
    row, col = uvLimits.shape[0:2]
    inPoints4 = np.zeros((row + 2, col), np.float32)
    inPoints4[0:2] = uvLimits
    inPoints4[2] =[1,1,1,1]
    inPoints3 = np.array(inPoints4)[0:3,:]
    
    c1 = cos(cameraInfo.pitch*pi/180)
    s1 = sin(cameraInfo.pitch*pi/180)
    c2 = cos(cameraInfo.yaw*pi/180)
    s2 = sin(cameraInfo.yaw*pi/180)

    matp= [
        [-cameraInfo.cameraHeight*c2/cameraInfo.focalLengthX,
        cameraInfo.cameraHeight*s1*s2/cameraInfo.focalLengthY,
        (cameraInfo.cameraHeight*c2*cameraInfo.opticalCenterX/cameraInfo.focalLengthX)
        -(cameraInfo.cameraHeight *s1*s2* cameraInfo.opticalCenterY/ cameraInfo.focalLengthY)
        -cameraInfo.cameraHeight *c1*s2],
        [cameraInfo.cameraHeight *s2/cameraInfo.focalLengthX,
        cameraInfo.cameraHeight *s1*c2/cameraInfo.focalLengthY,
        (-cameraInfo.cameraHeight *s2* cameraInfo.opticalCenterX
            /cameraInfo.focalLengthX)-(cameraInfo.cameraHeight *s1*c2*
            cameraInfo.opticalCenterY /cameraInfo.focalLengthY) - 
            cameraInfo.cameraHeight *c1*c2],
        [0, cameraInfo.cameraHeight *c1/cameraInfo.focalLengthY, (-cameraInfo.cameraHeight *c1* cameraInfo.opticalCenterY/cameraInfo.focalLengthY)+cameraInfo.cameraHeight*s1],
        [0, -c1 /cameraInfo.focalLengthY,(c1* cameraInfo.opticalCenterY /cameraInfo.focalLengthY) - s1]]

    inPoints4 = np.array(matp).dot(np.array(inPoints3))
    inPointsr4 = inPoints4[3,:]
    div = inPointsr4
    inPoints4[0,:] = inPoints4[0,:]/div
    inPoints4[1,:] = inPoints4[1,:]/div
    inPoints2 = inPoints4[0:2,:]
    xyLimits = inPoints2
    return xyLimits