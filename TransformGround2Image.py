# function [ uvGrid ] = TransformGround2Image( xyGrid, cameraInfo )
import numpy as np
from math import cos, sin, pi
def TransformGround2Image(xyGrid,cameraInfo):
    inPoints2 = xyGrid[0:2]
    inPointsr3 = np.ones((1,len(xyGrid[1])))*(-cameraInfo.cameraHeight)
    inPoints3 = np.concatenate((inPoints2, inPointsr3), axis=0)
    c1 = cos(cameraInfo.pitch*pi/180)
    s1 = sin(cameraInfo.pitch*pi/180)
    c2 = cos(cameraInfo.yaw*pi/180)
    s2 = sin(cameraInfo.yaw*pi/180)

    matp = [[cameraInfo.focalLengthX * c2 + c1*s2* cameraInfo.opticalCenterX,
        -cameraInfo.focalLengthX * s2 + c1*c2* cameraInfo.opticalCenterX,
        -s1 * cameraInfo.opticalCenterX],
        [s2 * (-cameraInfo.focalLengthY * s1 + c1* cameraInfo.opticalCenterY),
        c2 * (-cameraInfo.focalLengthY * s1 + c1* cameraInfo.opticalCenterY),
        -cameraInfo.focalLengthY * c1 - s1* cameraInfo.opticalCenterY],
        [c1*s2, c1*c2, -s1]]
    inPoints3 = np.array(matp).dot(np.array(inPoints3))
    inPointsr3 = inPoints3[2,:]
    div = inPointsr3
    inPoints3[0,:] = inPoints3[0,:]/div
    inPoints3[1,:] = inPoints3[1,:]/div
    inPoints2 = inPoints3[0:2,:]
    uvGrid = inPoints2
    return uvGrid