#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# readsp3        : Read the precision ephemeris file
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.03
# Latest Version : 2022.06.03 - Version 1.00

import datetime
import os
import sys


# 2022.06.03 : 精密星历文件中记录时间的行转为datetime格式
#              by ChangChuntao -> Version : 1.00
def sp3FileTimeLine2Datetime(line):
    line = line[3:]
    year = int(line.split()[0])
    month = int(line.split()[1])
    day = int(line.split()[2])
    hour = int(line.split()[3])
    minute = int(line.split()[4])
    second = int(float(line.split()[5]))
    microsecond = int(float(float(line.split()[5]) - second) * 1000.0)
    sp3DataTime = datetime.datetime(year, month, day, hour, minute, second, microsecond)
    return sp3DataTime


# 2022.06.03 : 读取精密星历头文件
#              by ChangChuntao -> Version : 1.00
def readSp3Head(sp3file):
    # 返回值p3Head定义为字典，其中字段：datetime & datetime格式时间; epoch & 历元列表; prn & 卫星prn号列表
    if os.path.isfile(sp3file):  # 文件不存在则退出
        sp3Head = {}
    else:
        print('File Not Exist!')
        sys.exit()

    # 读取所有数据至sp3FileLine
    sp3FileLine = open(sp3file, 'r+').readlines()

    # 读取首行中历元信息，存为datetime字段
    sp3Head['datetime'] = sp3FileTimeLine2Datetime(sp3FileLine[0])

    # 读取头文件中所有prn，存为prn字段
    # 读取sp3文件中所有历元，存为epoch字段
    epoch = []
    Sat = []
    for line in sp3FileLine[2:]:
        if line[0:2] == '+ ':  # 头文件内遇到'+ '时，从第九个字符串开始为prn
            for index_sat in range(0, 17):  # 每行为17个卫星
                if line[index_sat * 3 + 9:index_sat * 3 + 12] != '  0':
                    Sat.append(line[index_sat * 3 + 9:index_sat * 3 + 12])
        elif line[0:2] == '* ':
            epoch.append(sp3FileTimeLine2Datetime(line))
    sp3Head['prn'] = Sat
    sp3Head['epoch'] = epoch
    return sp3Head


# 2022.06.03 : 读取精密星历文件，并返回为sp3Data
#              by ChangChuntao -> Version : 1.00
def readSp3(sp3File):
    from module.sp3Class import sp3Sat
    # 返回值sp3Data的第一维为prn号
    # 第二维为卫星对应每个历元下的信息，信息存储为定义成sp3Sat的class
    # 例如sp3Data中C01卫星的信息存储为：
    #   | [epoch1, x1, y1, z1, clk1, vx1, vy1, vz1] |
    #   | [epoch2, x2, y2, z2, clk2, vx2, vy2, vz2] |
    #   | [.......................................] |
    #   | [epochn, xn, yn, zn, clkn, vxn, vyn, vzn] |
    # 获取C01卫星第2个历元下卫星的x坐标，则表达为sp3Data['C01'][2].x
    # 获取G12卫星第5个历元下所在的t时间，则表达为sp3Data['G12'][5].epoch

    if os.path.isfile(sp3File):  # 文件不存在则退出
        sp3Data = {}
    else:
        print('File Not Exist!')
        sys.exit()

    # 读取精密星历头文件，获取基本信息
    sp3HeadData = readSp3Head(sp3File)

    # 读取所有数据至sp3FileLine
    sp3FileLine = open(sp3File, 'r+').readlines()

    # 获取每组数据开始行的行数，即为确定历元信息行在sp3FileLine中的位置，将其在sp3FileLine中的索引存入timeIndex中，最后一行为-1
    timeIndex = []
    for epoch in sp3HeadData['epoch']:
        findEpochStr = '*  ' + str(epoch.year) + str(epoch.month).rjust(3) + str(epoch.day).rjust(3) + \
                       str(epoch.hour).rjust(3) + str(epoch.minute).rjust(3) + ('%.8f' % float(epoch.second)).rjust(
            12) + '\n'
        timeIndex.append(sp3FileLine.index(findEpochStr))
    timeIndex.append(-1)

    # 循环获取每颗卫星的信息，并返回sp3Data
    for prn in sp3HeadData['prn']:
        sp3DataPrn = []
        for t in range(0, len(timeIndex) - 1):
            for line_index in range(timeIndex[t], timeIndex[t + 1]):
                line = sp3FileLine[line_index]
                if line.split()[0] == 'P' + prn:
                    nowEpoch = sp3HeadData['epoch'][t]
                    x = float(line.split()[1])
                    y = float(line.split()[2])
                    z = float(line.split()[3])
                    if len(line) < 65:
                        clk = 0.0
                    else:
                        clk = float(line.split()[4])
                    nextLine = sp3FileLine[line_index + 1]
                    if nextLine.split()[0] == 'V' + prn:
                        vx = float(nextLine.split()[1])
                        vy = float(nextLine.split()[2])
                        vz = float(nextLine.split()[3])
                    else:
                        vx = vy = vz = 0.0
                    sp3DataPrn.append(sp3Sat(nowEpoch, x, y, z, clk, vx, vy, vz))
                    break
        sp3Data[prn] = sp3DataPrn
    return sp3Data
