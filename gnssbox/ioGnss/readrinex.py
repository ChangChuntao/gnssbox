#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# readrinex      : Read Rinex
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.07.14
# Latest Version : 2022.07.14 - Version 1.00


# 2022.07.14 : 读取rinex文件时间转为datetime
#              by ChangChuntao -> Version : 1.00
def readrinexLineTime(line):
    import datetime
    line = str(line).split()
    year = int(line[1])
    month = int(line[2])
    day = int(line[3])
    hour = int(line[4])
    minute = int(line[5])
    second = int(float(line[6]))
    lineDatetime = datetime.datetime(year, month, day, hour, minute, second)
    return lineDatetime
    

# 2022.07.14 : 读取观测文件中卫星对应的时间
#              by ChangChuntao -> Version : 1.00
def getRinexSatTime(rinexFile):
    rinexFileLineOpen = open(rinexFile, 'r+')
    rinexFileLine = rinexFileLineOpen.readlines()
    rinexFileLineOpen.close()
    satList = []
    rinexSatTime = {}
    endHeadLineNum = 0
    for line in rinexFileLine:
        endHeadLineNum += 1
        if 'END OF HEADER' in line:
            endHeadLineNum += 1
            break
    for line in rinexFileLine[endHeadLineNum:]:
        satPrn = line[:3]
        if satPrn not in satList and line[0] != '>':
            satList.append(satPrn)
            rinexSatTime[satPrn] = []
    timeLine = []
    lineNum = 0
    for line in rinexFileLine:
        if line[0] == '>':
            timeLine.append(lineNum)
        lineNum += 1
    for lineNumIndex in range(0, len(timeLine) - 1):
        nowDateTime = readrinexLineTime(rinexFileLine[timeLine[lineNumIndex]])
        for line in rinexFileLine[timeLine[lineNumIndex] + 1:timeLine[lineNumIndex + 1]]:
            satPrn = line[:3]
            rinexSatTime[satPrn].append(nowDateTime)
    return rinexSatTime