#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# sp3Class       : Class of sp3
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.03
# Latest Version : 2022.06.03 - Version 1.00

# 2022.06.03 : 精密星历卫星类
#              by ChangChuntao -> Version : 1.00
class sp3Sat:
    def __init__(self, epoch, x, y, z, clk, vx, vy, vz):
        self.epoch = epoch
        self.x = x
        self.y = y
        self.z = z
        self.clk = clk
        self.vx = vx
        self.vy = vy
        self.vz = vz