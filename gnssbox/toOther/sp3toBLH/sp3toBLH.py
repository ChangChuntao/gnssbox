#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# sp3toBLH       : The satellite position ECEF changes to a geodetic coordinate system
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.07.25
# Latest Version : 2022.07.25 - Version 1.00


def sp3toBLH(sp3File, blhFile=None):
    from readSp3 import readSp3
    from xyz2blh import xyz2blh
    import math
    sp3Data = readSp3(sp3File)
    if blhFile is None:
        blhFile = str(sp3File).split('.')[0] + '.blh'
    blhFileWrite = open(blhFile, 'w+')
    for prn in sp3Data:
        for epoch in sp3Data[prn]:
            writeStr = prn + ' '
            writeStr += str(epoch.epoch.year) + ' ' + str(epoch.epoch.month).zfill(2) + ' ' + str(
                epoch.epoch.day).zfill(2) + ' ' + \
                        str(epoch.epoch.hour).zfill(2) + ' ' + str(epoch.epoch.minute).zfill(2) + (
                                    '%.6f' % epoch.epoch.second).rjust(10) + ' '
            [B, L, H] = xyz2blh(epoch.x, epoch.y, epoch.z, 'WGS84')

            writeStr += ('%.12E' % math.degrees(L)).rjust(22)
            writeStr += ('%.12E' % math.degrees(B)).rjust(22)
            writeStr += ('%.12E' % H).rjust(22)
            blhFileWrite.write(writeStr + '\n')
