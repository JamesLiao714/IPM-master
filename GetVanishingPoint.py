# function [ vp ] = GetVanishingPoint( cameraInfo )
import numpy as np
from math import cos, sin, pi
def GetVanishingPoint(cameraInfo):
    vpp = [[sin(cameraInfo.yaw*pi/180)/cos(cameraInfo.pitch*pi/180)],
        [cos(cameraInfo.yaw*pi/180)/cos(cameraInfo.pitch*pi/180)],
        [0]]

    tyawp = [[cos(cameraInfo.yaw*pi/180), -sin(cameraInfo.yaw*pi/180), 0],
            [sin(cameraInfo.yaw*pi/180), cos(cameraInfo.yaw*pi/180), 0],
            [0, 0, 1]]
			
    tpitchp = [[1, 0, 0],
            [0, -sin(cameraInfo.pitch*pi/180), -cos(cameraInfo.pitch*pi/180)],
            [0, cos(cameraInfo.pitch*pi/180), -sin(cameraInfo.pitch*pi/180)]]

    t1p = [[cameraInfo.focalLengthX, 0, cameraInfo.opticalCenterX],
		  [0, cameraInfo.focalLengthY, cameraInfo.opticalCenterY],
		  [0, 0, 1]]

    transform = np.array(tyawp).dot(np.array(tpitchp))
    transform = np.array(t1p).dot(transform)
    vp = transform.dot(np.array(vpp))
    return vp