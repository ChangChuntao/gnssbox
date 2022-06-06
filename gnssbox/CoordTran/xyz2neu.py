#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# xyz2neu        : Convert ECEF coordinates to local coordinates
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.06
# Latest Version : 2022.06.06 - Version 1.00

def xyz2neu(originX, originY, originZ, X, Y, Z, System):
    import math
    from gnssbox.coordTran.xyz2blh import xyz2blh
    deltaX = X - originX
    deltaY = Y - originY
    deltaZ = Z - originZ
    [lat, lon, h] = xyz2blh(originX, originY, originZ, System)
    north = (-math.sin(lat) * math.cos(lon) * deltaX -
             math.sin(lat) * math.sin(lon) * deltaY +
             math.cos(lat) * deltaZ)
    east = -math.sin(lon) * deltaX + math.cos(lon) * deltaY
    up = (math.cos(lat) * math.cos(lon) * deltaX +
          math.cos(lat) * math.sin(lon) * deltaY +
          math.sin(lat) * deltaZ)
    return north, east, up