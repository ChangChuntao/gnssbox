#!/usr/bin/python3
# coding=utf-8
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
    # navFile       : 广播星历文件
    # rinexFile     : 观测文件
    # checkFile     : 检查结果输出文件(可选)
    from gnssbox.ioGnss.readNav import getNavSatTime
    from gnssbox.ioGnss.readrinex import getRinexSatTime
    from gnssbox.lib.gnssTime import datetime2gnssTime
    # 获取广播星历中卫星的历元
    navSatTime = getNavSatTime(navFile)
    # 获取观测文件中卫星的观测历元
    rinexSatTime = getRinexSatTime(rinexFile)
    # 输出文件名
    if checkFile is None:
        checkFile = rinexFile + '.satCheck'
    checkFileWrite = open(checkFile, 'w+')
    # 新建检查结果字典
    satEpochNavLack = {}
    for rinexSat in rinexSatTime:
        satEpochNavLack[rinexSat] = []
    # 卫星循环
    for rinexSat in rinexSatTime:
        # 历元循环
        for rnxSatEpoch in rinexSatTime[rinexSat]:
            # 判断有无对应的广播星历数据
            satFlag = 0
            if rinexSat in navSatTime:
                for navSatEpoch in navSatTime[rinexSat]:
                    # 有两小时内的数据则判断为有
                    secondDif = (rnxSatEpoch - navSatEpoch).seconds + (rnxSatEpoch - navSatEpoch).days * 86400
                    if -7200 < secondDif < 7200:
                        satFlag = 1
                if satFlag == 0:
                    # 若无，则添加此历元到结果字典中
                    satEpochNavLack[rinexSat].append(rnxSatEpoch)
            else:
                # 若广播星历内无此卫星，则输出None
                satEpochNavLack[rinexSat] = None
    # 写入文件
    for sat in satEpochNavLack:
        # 若广播星历内无此卫星，则输出None
        if satEpochNavLack[sat] is None:
            checkFileWrite.write(sat + ' None\n')
        else:
            # 存在确实历元，以MJD形式输出
            if len(satEpochNavLack[sat]) != 0:
                line = sat + ' '
                for satEpoch in satEpochNavLack[sat]:
                    [satEpochMjd, satEpochSod] = datetime2gnssTime(satEpoch, 'MJDSOD')
                    satEpochMjdSod = satEpochMjd * 1.0 + satEpochSod / 86400.0
                    line += ('%.7f' % satEpochMjdSod).rjust(15)
                line += '\n'
                checkFileWrite.write(line)
