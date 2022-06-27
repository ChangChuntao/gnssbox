#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# sp3toClk       : Read the precision ephemeris file
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.25
# Latest Version : 2022.06.25 - Version 1.00


def sp3toClk(sp3File, clkFile):
    from gnssbox.ioGnss.readSp3 import readSp3
    from gnssbox.ioGnss.readSp3 import readSp3Head
    from gnssbox.ioGnss.writeClk import writeClk
    from gnssbox.module.clkClass import clkSat
    sp3DataHead = readSp3Head(sp3File)
    sp3Data = readSp3(sp3File)
    clkData = {'sat': {}, 'site' : {}}
    for prn in sp3DataHead['prn']:
        clkData['sat'][prn] = []
    
    for prn in sp3Data:
        clkDataPrn = []
        for prnEpoch in sp3Data[prn]:
            clkDataPrn.append(clkSat(prnEpoch.epoch, prnEpoch.clk, None))
        clkData['sat'][prn] = clkDataPrn
    
    writeClk(clkData, clkFile)
    
    