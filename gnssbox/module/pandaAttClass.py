#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# pandaAttClass  : Class of panda att
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.05
# Latest Version : 2022.06.05 - Version 1.00


# 2022.06.05 : panda att类
#              by ChangChuntao -> Version : 1.00
class pandaAtt:
    def __init__(self, mjd, sod, roll, pitch, yaw, modeValues, mode):
        from gnssbox.lib.gnssTime import gnssTimesTran
        self.mjd = mjd
        self.sod = sod
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.modeValues = modeValues
        self.mode = mode
        self.Time = gnssTimesTran(From = 'MJDSOD', To = 'DATETIME', Time = [mjd, sod])