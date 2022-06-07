#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# blh2xyz        : Conversion of ECEF coordinates to geodetic coordinates
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.06
# Latest Version : 2022.06.06 - Version 1.00

def blh2xyz(b, l, h, System):
    from gnssbox.lib.gnssParameter import coordSystem
    import math
    a = coordSystem[System].a
    e2 = coordSystem[System].e2
    N = a / math.sqrt(1 - e2 * (math.sin(b)) * (math.sin(b)))
    X = (N + h) * math.cos(b) * math.cos(l)
    Y = (N + h) * math.cos(b) * math.sin(l)
    Z = (N * (1 - e2) + h) * math.sin(b)
    return X, Y, Z