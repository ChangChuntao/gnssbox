#!/usr/bin/python3
# gnssbox           : The most complete GNSS Python toolkit ever
# Github            : https://github.com/ChangChuntao/gnssbox.git
# navSatCheck       : Gets the absence of epoch in broadcast ephemeris corresponding to satellites in rinex file
# Author            : Chang Chuntao 1252443496@qq.com
# Copyright(C)      : The GNSS Center, Wuhan University
# Creation Date     : 2022.07.14
# Latest Version    : 2022.07.14 - Version 1.00

# 2022.07.14 : 获取rinex文件内卫星所对应的广播星历内历元的缺失情况
#              by ChangChuntao -> Version : 1.00
def navSatCheck(navFile, rinexFile, checkFile=None):
    from gnssbox.ioGnss.readNav import getNavSatTime
    from gnssbox.ioGnss.readrinex import getRinexSatTime
    from gnssbox.lib.gnssTime import datetime2gnssTime

    navSatTime = getNavSatTime(navFile)
    rinexSatTime = getRinexSatTime(rinexFile)
    if checkFile is None:
        checkFile = rinexFile + '.satCheck'
    checkFileWrite = open(checkFile, 'w+')
    satEpochNavLack = {}
    for rinexSat in rinexSatTime:
        satEpochNavLack[rinexSat] = []

    for rinexSat in rinexSatTime:
        for rnxSatEpoch in rinexSatTime[rinexSat]:
            satFlag = 0
            if rinexSat in navSatTime:
                for navSatEpoch in navSatTime[rinexSat]:
                    secondDif = (rnxSatEpoch - navSatEpoch).seconds + (rnxSatEpoch - navSatEpoch).days * 86400
                    if -7200 < secondDif < 7200:
                        satFlag = 1
                if satFlag == 0:
                    satEpochNavLack[rinexSat].append(rnxSatEpoch)
            else:
                satEpochNavLack[rinexSat] = None
    for sat in satEpochNavLack:
        if satEpochNavLack[sat] is None:
            checkFileWrite.write(sat + ' None\n')
        else:
            if len(satEpochNavLack[sat]) != 0:
                line = sat + ' '
                for satEpoch in satEpochNavLack[sat]:
                    [satEpochMjd, satEpochSod] = datetime2gnssTime(satEpoch, 'MJDSOD')
                    satEpochMjdSod = satEpochMjd * 1.0 + satEpochSod / 86400.0
                    line += ('%.7f' % satEpochMjdSod).rjust(15)
                line += '\n'
                checkFileWrite.write(line)
