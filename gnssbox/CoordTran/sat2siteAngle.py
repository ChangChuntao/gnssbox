#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# sat2siteAngle  : Calculate the Angle between site and satellite
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.03
# Latest Version : 2022.06.03 - Version 1.00


def sat2siteAngle(satX, satY, satZ, siteX, siteY, siteZ):
    import math
    from gnssbox.coordTran.xyz2neu import xyz2neu
    from gnssbox.coordTran.xyz2blh import xyz2blh
    from gnssbox.coordTran.xy2azi import xy2azi
    System = 'WGS84'
    north, east, up = xyz2neu(siteX, siteY, siteZ, satX, satY, satZ, System)
    siteB, siteL, H = xyz2blh(siteX, siteY, siteZ, System)
    satB, satL, H = xyz2blh(satX, satY, satZ, System)
    Azimuth = xy2azi(siteL, siteB, satL, satB)
    Elevation = math.atan(up / math.sqrt(north * north + east * east))
    Zenith = math.pi / 2 - Elevation
    return Zenith, Azimuth, Elevation
