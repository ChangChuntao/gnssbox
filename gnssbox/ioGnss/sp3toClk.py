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
    sp3Head = readSp3Head(sp3File)
    sp3Data = readSp3(sp3File)
    clkData = {'sat': {}, 'site' : {}}
    clkHead = {'RINEX VERSION': 3.00, 'PGM': 'GNSSBOX', 'INTERVAL': None, 'RUN BY': 'WHU@CCT', 'DATE': '', 'TYPES OF DATA': ['AS'],
               'ANALYSIS CENTER': 'WHU  GNSS RESEARCH CENTER, WUHAN UNIVERSITY, P.R.CHINA', 'SOLN SATS': sp3Head['prn'],
               'epochList': sp3Head['epoch']}
    
    for prn in sp3Data:
        clkDataPrn = []
        for prnEpoch in sp3Data[prn]:
            clkDataPrn.append(clkSat(prnEpoch.epoch, prnEpoch.clk/1000000, None))
        clkData['sat'][prn] = clkDataPrn
    
    writeClk(clkHead, clkData, clkFile)
    
    