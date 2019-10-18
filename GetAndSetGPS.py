from fractions import Fraction
import piexif
import exifread
import os
from PIL import Image

def ParseGPSExpress(gps_express):
    '''
    GPS座標表達式轉數值
    :param gps_express: GPS座標表達式 [1,2,3/4]
    :return: GPS座標數值 1.033542
    '''
    try:
        express = str(gps_express).replace(" ", "").replace("[", "").replace("]", "")
        parts = express.split(",")
        subpart = parts[2].split("/")

        degrees = float(parts[0])
        minutes = float(parts[1])
        seconds = float(subpart[0]) / float(subpart[1])
        return degrees + minutes / 60 + seconds / 3600
    except:
        raise Exception("Error information for the picture")


def PhotoGPS(photoPath, ipmPhotoPath):
    '''
    照片拍攝地GPS座標
    :param photoPath: 照片的磁盤路徑
    :return: 照片的 （GPS經度，GPS緯度）
    '''
    if not os.path.isfile(photoPath):
        raise Exception("File is not exist")

    with open(photoPath, 'rb') as f:
        exifDict = exifread.process_file(f)
        longitudeRef = str(exifDict["GPS GPSLongitudeRef"]).strip()
        longitude = ParseGPSExpress(str(exifDict["GPS GPSLongitude"]))
        latitudeRef = str(exifDict["GPS GPSLatitudeRef"]).strip()
        latitude = ParseGPSExpress(str(exifDict["GPS GPSLatitude"]))

    lng = longitude if "E" == longitudeRef else 0 - longitude
    lat = latitude if "N" == latitudeRef else 0 - latitude
    print(exifDict['EXIF ExifImageWidth'], exifDict['EXIF ExifImageLength'], exifDict['EXIF FocalLength'], exifDict['EXIF ApertureValue'])
    # SetGPSLocation(ipmPhotoPath, lat, lng)
    return lng, lat

def ToDeg(value, loc):
    """convert decimal coordinates into degrees, munutes and seconds tuple
    Keyword arguments: value is float gps-value, loc is direction list ["S", "N"] or ["W", "E"]
    return: tuple like (25, 13, 48.343 ,'N')
    """
    if value < 0:
        locValue = loc[0]
    elif value > 0:
        locValue = loc[1]
    else:
        locValue = ""
    absValue = abs(value)
    deg =  int(absValue)
    t1 = (absValue-deg)*60
    min = int(t1)
    sec = round((t1 - min)* 60, 5)
    return (deg, min, sec, locValue)


def ChangeToRational(number):
    """convert a number to rantional
    Keyword arguments: number
    return: tuple like (1, 2), (numerator, denominator)
    """
    f = Fraction(str(number))
    return (f.numerator, f.denominator)


def SetGPSLocation(fileName, lat, lng): # altitude
    """Adds GPS position as EXIF metadata
    Keyword arguments:
    fileName -- image file
    lat -- latitude (as float)
    lng -- longitude (as float)
    altitude -- altitude (as float)
    """
    latDeg = ToDeg(lat, ["S", "N"])
    lngDeg = ToDeg(lng, ["W", "E"])

    exivLat = (ChangeToRational(latDeg[0]), ChangeToRational(latDeg[1]), ChangeToRational(latDeg[2]))
    exivLng = (ChangeToRational(lngDeg[0]), ChangeToRational(lngDeg[1]), ChangeToRational(lngDeg[2]))

    gpsIfd = {
        piexif.GPSIFD.GPSVersionID: (2, 0, 0, 0),
        piexif.GPSIFD.GPSAltitudeRef: 1,
        # piexif.GPSIFD.GPSAltitude: ChangeToRational(round(altitude)),
        piexif.GPSIFD.GPSLatitudeRef: latDeg[3],
        piexif.GPSIFD.GPSLatitude: exivLat,
        piexif.GPSIFD.GPSLongitudeRef: lngDeg[3],
        piexif.GPSIFD.GPSLongitude: exivLng,
    }

    exifDict = {"GPS": gpsIfd}
    exifBytes = piexif.dump(exifDict)
    piexif.insert(exifBytes, fileName)


def TransferGPS(photoPath, ipmPhotoPath):
    img = Image.open(photoPath)
    exifDict = piexif.load(img.info['exif'])
    exifDict = {"GPS": exifDict['GPS']}
    exifBytes = piexif.dump(exifDict)
    piexif.insert(exifBytes, ipmPhotoPath)

i = 4
photoPath = 'Images/road' + str(i) + '.jpg'
ipmPhotoPath = 'Images/road' + str(i) + '_ipm.png'
PhotoGPS(photoPath, ipmPhotoPath)

