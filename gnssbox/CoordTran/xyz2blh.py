#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# xyz2blh        : Conversion of ECEF coordinates to geodetic coordinates
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.06
# Latest Version : 2022.06.06 - Version 1.00


def xyz2blh(X, Y, Z, System):
    import math
    from gnssbox.lib.gnssParameter import coordSystem
    a = coordSystem[System].a
    e2 = coordSystem[System].e2
    b = coordSystem[System].b
    L = math.atan2(Y, X)
    N0 = a
    H0 = math.sqrt(X * X + Y * Y + Z * Z) - math.sqrt(a * b)
    B0 = math.atan(Z / math.sqrt(X * X + Y * Y) / (1.0 - e2 * N0 / (N0 + H0)))
    while True:
        N1 = a / math.sqrt(1.0 - e2 * (math.sin(B0) ** 2.0))
        H = math.sqrt(X ** 2.0 + Y ** 2.0) / math.cos(B0) - N1
        B = math.atan(Z / math.sqrt(X * X + Y * Y) / (1.0 - e2 * N1 / (N1 + H)))
        if abs(H - H0) > 0.0001 and abs(B - B0) > 1.0e-10:
            N0 = N1
            H0 = H
            B0 = B
        else:
            break
    return B, L, H
