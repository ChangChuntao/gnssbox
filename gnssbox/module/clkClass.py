#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# clkClass       : Class of clk
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.27
# Latest Version : 2022.06.27 - Version 1.00

# 2022.06.27 : 钟差卫星类
#              by ChangChuntao -> Version : 1.00
class clkSat:
    def __init__(self, epoch, clk, clkMerror):
        self.epoch = epoch
        self.clk = clk
        self.clkMerror = clkMerror

# 2022.06.27 : 钟差站点类
#              by ChangChuntao -> Version : 1.00
class clkSite:
    def __init__(self, epoch, clk, clkMerror):
        self.epoch = epoch
        self.clk = clk
        self.clkMerror = clkMerror