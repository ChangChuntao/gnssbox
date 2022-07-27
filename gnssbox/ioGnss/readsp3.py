#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# readsp3        : Read the precision ephemeris file
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.03
# Latest Version : 2022.06.03 - Version 1.00


# 2022.06.03 : 精密星历文件中记录时间的行转为datetime格式
#              by ChangChuntao -> Version : 1.00
def sp3FileTimeLine2Datetime(line):
    import datetime
    line = line[3:]
    year = int(line.split()[0])
    month = int(line.split()[1])
    day = int(line.split()[2])
    hour = int(line.split()[3])
    minute = int(line.split()[4])
    second = int(str(line.split()[5]).split('.')[0])
    microsecond = int(int(str(line.split()[5]).split('.')[-1]) / 100)
    sp3DataTime = datetime.datetime(year, month, day, hour, minute, second, microsecond)
    return sp3DataTime


# 2022.06.03 : 读取精密星历头文件
#              by ChangChuntao -> Version : 1.00
def readSp3Head(sp3file):
    import os
    import sys
    # sp3Head：定义为字典
    # 其中字段：datetime & datetime格式时间; epoch & 历元列表; prn & 卫星prn号列表
    if os.path.isfile(sp3file):  # 文件不存在则退出
        sp3Head = {}
    else:
        print('File Not Exist!')
        sys.exit()

    # 读取所有数据至sp3FileLine
    sp3FileLine = open(sp3file, 'r+').readlines()
    epoch = []
    Sat = []
    SatPrecision = []
    cfi = []
    comment = []
    for line in sp3FileLine[2:]:
        if line[0:2] == '+ ':  # 头文件内遇到'+ '时，从第九个字符串开始为prn
            for index_sat in range(0, 17):  # 每行为17个卫星
                if line[index_sat * 3 + 9:index_sat * 3 + 12] != '  0':
                    Sat.append(line[index_sat * 3 + 9:index_sat * 3 + 12])
        elif line[0:2] == '%c' or line[0:2] == '%f' or line[0:2] == '%i':
            cfi.append(line)
        elif line[0:2] == r'/*':
            comment.append(line)
        elif line[0:2] == '* ':
            epoch.append(sp3FileTimeLine2Datetime(line))
    satLineNum = int(len(Sat) / 17)
    lastSatNum = len(Sat) - int(len(Sat) / 17) * 17
    satLineCounter = 0
    for line in sp3FileLine[2:]:
        if line[0:2] == '++' and satLineCounter == satLineNum:
            inLine = line.split()[1:lastSatNum + 1]
            for pre in inLine:
                SatPrecision.append(int(pre))
            break
        if line[0:2] == '++' and satLineCounter < satLineNum:  # 头文件内遇到'++'时，从第九个字符串开始为sat pre
            satLineCounter += 1
            inLine = line.split()[1:]
            for pre in inLine:
                SatPrecision.append(int(pre))

    print(len(SatPrecision))
    # 读取首行中历元信息，存为datetime字段
    sp3Head['datetime'] = sp3FileTimeLine2Datetime(sp3FileLine[0])
    # 读取首行历元数
    sp3Head['epochNum'] = int(sp3FileLine[0].split()[6])
    # 读取首行参考系统
    sp3Head['RefSystem'] = sp3FileLine[0].split()[8]
    # 读取首个历元时间格式
    sp3Head['firstTime'] = {}
    sp3Head['firstTime']['gpsWeek'] = int(sp3FileLine[1].split()[1])
    sp3Head['firstTime']['gpsSow'] = float(sp3FileLine[1].split()[2])
    sp3Head['firstTime']['interval'] = float(sp3FileLine[1].split()[3])
    sp3Head['firstTime']['mjd'] = int(sp3FileLine[1].split()[4])
    sp3Head['firstTime']['sod'] = float(sp3FileLine[1].split()[5])
    # 读取头文件中所有prn，存为prn字段
    sp3Head['prn'] = Sat
    # 读取头文件中卫星精度信息，存为satPre字段
    sp3Head['satPre'] = SatPrecision
    # 读取sp3文件中所有历元，存为epoch字段
    sp3Head['epoch'] = epoch
    # %c %f %i
    sp3Head['cfi'] = cfi
    # 备注信息
    sp3Head['comment'] = comment
    return sp3Head


# 2022.06.03 : 读取精密星历文件，并返回为sp3Data
#              by ChangChuntao -> Version : 1.00
def readSp3(sp3File):
    import os
    import sys
    from gnssbox.module.sp3Class import sp3Sat
    # sp3Data：
    #   第一维为prn号
    #   第二维为卫星对应每个历元下的信息，信息存储为定义成sp3Sat的class
    #       例如sp3Data中C01卫星的信息存储为：
    #           | [epoch1, x1, y1, z1, clk1, vx1, vy1, vz1] |
    #           | [epoch2, x2, y2, z2, clk2, vx2, vy2, vz2] |
    #           | [.......................................] |
    #           | [epochn, xn, yn, zn, clkn, vxn, vyn, vzn] |
    # 获取C01卫星第2个历元下卫星的x坐标，则表达为sp3Data['C01'][2].x
    # 获取G12卫星第5个历元下所在的t时间，则表达为sp3Data['G12'][5].epoch

    if os.path.isfile(sp3File):  # 文件不存在则退出
        sp3Data = {}
    else:
        print('File Not Exist!')
        sys.exit()

    # 读取精密星历头文件，获取基本信息
    sp3HeadData = readSp3Head(sp3File)
    for prn in sp3HeadData['prn']:
        sp3Data[prn] = []
    # 读取所有数据至sp3FileLine
    sp3FileLine = open(sp3File, 'r+').readlines()

    for lineNum in range(0, len(sp3FileLine)):
        if sp3FileLine[lineNum][0] == '*':
            nowEpoch = sp3FileTimeLine2Datetime(sp3FileLine[lineNum])
        if sp3FileLine[lineNum][0] == 'P':
            prn = sp3FileLine[lineNum].split()[0][1:]
            x = float(sp3FileLine[lineNum].split()[1]) * 1000.0
            y = float(sp3FileLine[lineNum].split()[2]) * 1000.0
            z = float(sp3FileLine[lineNum].split()[3]) * 1000.0
            if len(sp3FileLine[lineNum]) < 55:
                clk = 0.0
            else:
                clk = float(sp3FileLine[lineNum].split()[4])
            if sp3FileLine[lineNum + 1][0] == 'V':
                vx = float(sp3FileLine[lineNum + 1].split()[1]) * 10.0
                vy = float(sp3FileLine[lineNum + 1].split()[2]) * 10.0
                vz = float(sp3FileLine[lineNum + 1].split()[3]) * 10.0
            else:
                vx = vy = vz = 0.0
            sp3Data[prn].append(sp3Sat(nowEpoch, x, y, z, clk, vx, vy, vz))
    return sp3Data
