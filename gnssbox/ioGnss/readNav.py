#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# readNav        : Read the broadcast ephemeris file
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.07.14
# Latest Version : 2022.07.14 - Version 1.00

# 2022.06.03 : 精密星历文件中记录时间的行转为datetime格式
#              by ChangChuntao -> Version : 1.00
def navFileTimeLine2Datetime(line):
    import datetime
    line = line[3:]
    year = int(line.split()[0])
    month = int(line.split()[1])
    day = int(line.split()[2])
    hour = int(line.split()[3])
    minute = int(line.split()[4])
    second = int(line[18:20])
    navDataTime = datetime.datetime(year, month, day, hour, minute, second)
    return navDataTime


# 2022.07.14 : 广播星历数据
#              by ChangChuntao -> Version : 1.00
def readNavHead(navFile):
    navFileLineOpen = open(navFile, 'r+')
    navFileLine = navFileLineOpen.readlines()
    navFileLineOpen.close()
    navHeadData = {}
    rinexVersion = float(navFileLine[0].split()[0])
    navHeadData['RINEX VERSION'] = rinexVersion
    navHeadData['First Line'] = navFileLine[0]
    for line in navFileLine:
        if 'END OF HEADER' in line:
            break
        elif 'PGM' in line:
            navHeadData['PGM Line'] = navFileLine[1]
        elif 'LEAP SECONDS' in line:
            navHeadData['LEAP SECONDS'] = int(line.split()[0])
    return navHeadData


# 2022.07.14 : 广播星历基本信息
#              by ChangChuntao -> Version : 1.00
def getNavSatTime(navFile):
    navFileLineOpen = open(navFile, 'r+')
    navFileLine = navFileLineOpen.readlines()
    navFileLineOpen.close()

    endHeadLine = 0
    satSystem = ['C', 'R', 'G', 'E', 'I', 'S', 'J']
    for line in navFileLine:
        endHeadLine += 1
        if 'END OF HEADER' in line:
            break
    lineNum = endHeadLine
    navHead = {}
    satList = []
    while True:
        if lineNum < len(navFileLine) - 1:
            lineNum += 1
            if navFileLine[lineNum][0] in satSystem:
                if navFileLine[lineNum][:3] not in satList:
                    satList.append(navFileLine[lineNum][:3])
                    navHead[navFileLine[lineNum][:3]] = []
        else:
            break
    lineNum = endHeadLine
    while True:
        if lineNum < len(navFileLine) - 1:
            lineNum += 1
            if navFileLine[lineNum][0] in satSystem:
                nowTime = navFileTimeLine2Datetime(navFileLine[lineNum])

                navHead[navFileLine[lineNum][:3]].append(nowTime)
        else:
            break
    return navHead


# 2022.07.14 : 广播星历数据
#              by ChangChuntao -> Version : 1.00
def readNav(navFile):
    from gnssbox.module.navClass import bdsNav, gpsNav, galileoNav, glonassNav, irnssNav, sbasNav, qzssNav
    navSatTime = getNavSatTime(navFile)
    navFileLineOpen = open(navFile, 'r+')
    navFileLine = navFileLineOpen.readlines()
    navFileLineOpen.close()
    rinexVer = float(navFileLine[0].split()[0])
    endHeadLine = 0
    for line in navFileLine:
        endHeadLine += 1
        if 'END OF HEADER' in line:
            break
    navData = {}
    for sat in navSatTime:
        navData[sat] = []
    lineNum = endHeadLine
    while lineNum < len(navFileLine):
        sat = navFileLine[lineNum][:3]
        epoch = navFileTimeLine2Datetime(navFileLine[lineNum])
        if sat[0] == 'C':
            SVclockBias = float(navFileLine[lineNum][23:42])
            SVclockDrift = float(navFileLine[lineNum][42:61])
            SVclockDriftRate = float(navFileLine[lineNum][61:80])

            AODE = float(navFileLine[lineNum + 1][4:23])
            Crs = float(navFileLine[lineNum + 1][23:42])
            DeltaN = float(navFileLine[lineNum + 1][42:61])
            M0 = float(navFileLine[lineNum + 1][61:80])

            Cuc = float(navFileLine[lineNum + 2][4:23])
            e = float(navFileLine[lineNum + 2][23:42])
            Cus = float(navFileLine[lineNum + 2][42:61])
            sqrtA = float(navFileLine[lineNum + 2][61:80])

            toe = float(navFileLine[lineNum + 3][4:23])
            Cic = float(navFileLine[lineNum + 3][23:42])
            OMEGA0 = float(navFileLine[lineNum + 3][42:61])
            Cis = float(navFileLine[lineNum + 3][61:80])

            i0 = float(navFileLine[lineNum + 4][4:23])
            Crc = float(navFileLine[lineNum + 4][23:42])
            omega = float(navFileLine[lineNum + 4][42:61])
            OMEGA_DOT = float(navFileLine[lineNum + 4][61:80])

            IDOT = float(navFileLine[lineNum + 5][4:23])
            Spare1 = 0.0
            BDT_Week = float(navFileLine[lineNum + 5][42:61])
            Spare2 = 0.0

            SVaccuracy = float(navFileLine[lineNum + 6][4:23])
            SatH1 = float(navFileLine[lineNum + 6][23:42])
            TGD1 = float(navFileLine[lineNum + 6][42:61])
            TGD2 = float(navFileLine[lineNum + 6][61:80])

            Transmission = float(navFileLine[lineNum + 7][4:23])
            AODC = float(navFileLine[lineNum + 7][23:42])
            lineNum += 8
            navData[sat].append(bdsNav(epoch, SVclockBias, SVclockDrift, SVclockDriftRate,
                                       AODE, Crs, DeltaN, M0, Cuc, e, Cus,
                                       sqrtA, toe, Cic, OMEGA0, Cis,
                                       i0, Crc, omega, OMEGA_DOT, IDOT, Spare1, BDT_Week, Spare2,
                                       SVaccuracy, SatH1, TGD1, TGD2, Transmission, AODC))
        elif sat[0] == 'G':
            SVclockBias = float(navFileLine[lineNum][23:42])
            SVclockDrift = float(navFileLine[lineNum][42:61])
            SVclockDriftRate = float(navFileLine[lineNum][61:80])

            IODE = float(navFileLine[lineNum + 1][4:23])
            Crs = float(navFileLine[lineNum + 1][23:42])
            DeltaN = float(navFileLine[lineNum + 1][42:61])
            M0 = float(navFileLine[lineNum + 1][61:80])

            Cuc = float(navFileLine[lineNum + 2][4:23])
            e = float(navFileLine[lineNum + 2][23:42])
            Cus = float(navFileLine[lineNum + 2][42:61])
            sqrtA = float(navFileLine[lineNum + 2][61:80])

            toe = float(navFileLine[lineNum + 3][4:23])
            Cic = float(navFileLine[lineNum + 3][23:42])
            OMEGA0 = float(navFileLine[lineNum + 3][42:61])
            Cis = float(navFileLine[lineNum + 3][61:80])

            i0 = float(navFileLine[lineNum + 4][4:23])
            Crc = float(navFileLine[lineNum + 4][23:42])
            omega = float(navFileLine[lineNum + 4][42:61])
            OMEGA_DOT = float(navFileLine[lineNum + 4][61:80])

            IDOT = float(navFileLine[lineNum + 5][4:23])
            L2Codes = float(navFileLine[lineNum + 5][23:42])
            GPS_Week = float(navFileLine[lineNum + 5][42:61])
            L2PdataFlag = float(navFileLine[lineNum + 5][61:80])

            SVaccuracy = float(navFileLine[lineNum + 6][4:23])
            SVhealth = float(navFileLine[lineNum + 6][23:42])
            TGD = float(navFileLine[lineNum + 6][42:61])
            IODC = float(navFileLine[lineNum + 6][61:80])

            Transmission = float(navFileLine[lineNum + 7][4:23])
            if len(navFileLine[lineNum + 7]) < 42 or navFileLine[lineNum + 7][23:42] == '' or \
                    navFileLine[lineNum + 7][23:42] == '                   ':
                FitIntervalHours = 0.0
            else:
                FitIntervalHours = float(navFileLine[lineNum + 7][23:42])
            lineNum += 8
            navData[sat].append(gpsNav(epoch, SVclockBias, SVclockDrift, SVclockDriftRate,
                                       IODE, Crs, DeltaN, M0, Cuc, e, Cus,
                                       sqrtA, toe, Cic, OMEGA0, Cis,
                                       i0, Crc, omega, OMEGA_DOT, IDOT, L2Codes, GPS_Week, L2PdataFlag,
                                       SVaccuracy, SVhealth, TGD, IODC, Transmission, FitIntervalHours))
        elif sat[0] == 'E':
            SVclockBias = float(navFileLine[lineNum][23:42])
            SVclockDrift = float(navFileLine[lineNum][42:61])
            SVclockDriftRate = float(navFileLine[lineNum][61:80])

            IODnav = float(navFileLine[lineNum + 1][4:23])
            Crs = float(navFileLine[lineNum + 1][23:42])
            DeltaN = float(navFileLine[lineNum + 1][42:61])
            M0 = float(navFileLine[lineNum + 1][61:80])

            Cuc = float(navFileLine[lineNum + 2][4:23])
            e = float(navFileLine[lineNum + 2][23:42])
            Cus = float(navFileLine[lineNum + 2][42:61])
            sqrtA = float(navFileLine[lineNum + 2][61:80])

            toe = float(navFileLine[lineNum + 3][4:23])
            Cic = float(navFileLine[lineNum + 3][23:42])
            OMEGA0 = float(navFileLine[lineNum + 3][42:61])
            Cis = float(navFileLine[lineNum + 3][61:80])

            i0 = float(navFileLine[lineNum + 4][4:23])
            Crc = float(navFileLine[lineNum + 4][23:42])
            omega = float(navFileLine[lineNum + 4][42:61])
            OMEGA_DOT = float(navFileLine[lineNum + 4][61:80])

            IDOT = float(navFileLine[lineNum + 5][4:23])
            DataSources = float(navFileLine[lineNum + 5][23:42])
            GAL_Week = float(navFileLine[lineNum + 5][42:61])
            Spare = 0.0

            SISA = float(navFileLine[lineNum + 6][4:23])
            SVhealth = float(navFileLine[lineNum + 6][23:42])
            BGD_E5a_E1 = float(navFileLine[lineNum + 6][42:61])
            BGD_E5b_E1 = float(navFileLine[lineNum + 6][61:80])

            Transmission = float(navFileLine[lineNum + 7][4:23])

            lineNum += 8
            navData[sat].append(galileoNav(epoch, SVclockBias, SVclockDrift, SVclockDriftRate,
                                           IODnav, Crs, DeltaN, M0, Cuc, e, Cus,
                                           sqrtA, toe, Cic, OMEGA0, Cis,
                                           i0, Crc, omega, OMEGA_DOT, IDOT, DataSources, GAL_Week, Spare,
                                           SISA, SVhealth, BGD_E5a_E1, BGD_E5b_E1, Transmission))
        elif sat[0] == 'R':
            SVclockBias = float(navFileLine[lineNum][23:42])
            SVrelativeFrequencyBias = float(navFileLine[lineNum][42:61])
            MessageFrameTime = float(navFileLine[lineNum][61:80])

            posX = float(navFileLine[lineNum + 1][4:23])
            velX = float(navFileLine[lineNum + 1][23:42])
            accelerationX = float(navFileLine[lineNum + 1][42:61])
            health = float(navFileLine[lineNum + 1][61:80])

            posY = float(navFileLine[lineNum + 2][4:23])
            velY = float(navFileLine[lineNum + 2][23:42])
            accelerationY = float(navFileLine[lineNum + 2][42:61])
            frequency = float(navFileLine[lineNum + 2][61:80])

            posZ = float(navFileLine[lineNum + 3][4:23])
            velZ = float(navFileLine[lineNum + 3][23:42])
            accelerationZ = float(navFileLine[lineNum + 3][42:61])
            operAge = float(navFileLine[lineNum + 3][61:80])
            if rinexVer > 3.04:
                StatusFlags = float(navFileLine[lineNum + 4][4:23])
                delayDif = float(navFileLine[lineNum + 4][23:42])
                URAI = float(navFileLine[lineNum + 4][42:61])
                HealthFlags = float(navFileLine[lineNum + 4][61:80])
                lineNum += 5
            else:
                StatusFlags = 0.0
                delayDif = 0.0
                URAI = 0.0
                HealthFlags = 0.0
                lineNum += 4

            navData[sat].append(glonassNav(epoch, SVclockBias, SVrelativeFrequencyBias, MessageFrameTime,
                                           posX, velX, accelerationX, health,
                                           posY, velY, accelerationY, frequency,
                                           posZ, velZ, accelerationZ, operAge,
                                           StatusFlags, delayDif, URAI, HealthFlags))
        elif sat[0] == 'J':
            SVclockBias = float(navFileLine[lineNum][23:42])
            SVclockDrift = float(navFileLine[lineNum][42:61])
            SVclockDriftRate = float(navFileLine[lineNum][61:80])

            IODE = float(navFileLine[lineNum + 1][4:23])
            Crs = float(navFileLine[lineNum + 1][23:42])
            DeltaN = float(navFileLine[lineNum + 1][42:61])
            M0 = float(navFileLine[lineNum + 1][61:80])

            Cuc = float(navFileLine[lineNum + 2][4:23])
            e = float(navFileLine[lineNum + 2][23:42])
            Cus = float(navFileLine[lineNum + 2][42:61])
            sqrtA = float(navFileLine[lineNum + 2][61:80])

            toe = float(navFileLine[lineNum + 3][4:23])
            Cic = float(navFileLine[lineNum + 3][23:42])
            OMEGA0 = float(navFileLine[lineNum + 3][42:61])
            Cis = float(navFileLine[lineNum + 3][61:80])

            i0 = float(navFileLine[lineNum + 4][4:23])
            Crc = float(navFileLine[lineNum + 4][23:42])
            omega = float(navFileLine[lineNum + 4][42:61])
            OMEGA_DOT = float(navFileLine[lineNum + 4][61:80])

            IDOT = float(navFileLine[lineNum + 5][4:23])
            L2Codes = float(navFileLine[lineNum + 5][23:42])
            GPS_Week = float(navFileLine[lineNum + 5][42:61])
            L2PdataFlag = float(navFileLine[lineNum + 5][61:80])

            SVaccuracy = float(navFileLine[lineNum + 6][4:23])
            SVhealth = float(navFileLine[lineNum + 6][23:42])
            TGD = float(navFileLine[lineNum + 6][42:61])
            IODC = float(navFileLine[lineNum + 6][61:80])

            Transmission = float(navFileLine[lineNum + 7][4:23])
            FitIntervalFlag = float(navFileLine[lineNum + 7][23:42])

            lineNum += 8
            navData[sat].append(qzssNav(epoch, SVclockBias, SVclockDrift, SVclockDriftRate,
                                        IODE, Crs, DeltaN, M0, Cuc, e, Cus,
                                        sqrtA, toe, Cic, OMEGA0, Cis,
                                        i0, Crc, omega, OMEGA_DOT, IDOT, L2Codes, GPS_Week, L2PdataFlag,
                                        SVaccuracy, SVhealth, TGD, IODC, Transmission, FitIntervalFlag))
        elif sat[0] == 'S':
            SVclockBias = float(navFileLine[lineNum][23:42])
            SVrelativeFrequencyBias = float(navFileLine[lineNum][42:61])
            Transmission = float(navFileLine[lineNum][61:80])

            posX = float(navFileLine[lineNum + 1][4:23])
            velX = float(navFileLine[lineNum + 1][23:42])
            accelerationX = float(navFileLine[lineNum + 1][42:61])
            health = float(navFileLine[lineNum + 1][61:80])

            posY = float(navFileLine[lineNum + 2][4:23])
            velY = float(navFileLine[lineNum + 2][23:42])
            accelerationY = float(navFileLine[lineNum + 2][42:61])
            AccuracyCode = float(navFileLine[lineNum + 2][61:80])

            posZ = float(navFileLine[lineNum + 3][4:23])
            velZ = float(navFileLine[lineNum + 3][23:42])
            accelerationZ = float(navFileLine[lineNum + 3][42:61])
            IODN = float(navFileLine[lineNum + 3][61:80])

            lineNum += 4
            navData[sat].append(sbasNav(epoch, SVclockBias, SVrelativeFrequencyBias, Transmission,
                                        posX, velX, accelerationX, health,
                                        posY, velY, accelerationY, AccuracyCode,
                                        posZ, velZ, accelerationZ, IODN))
        elif sat[0] == 'I':
            SVclockBias = float(navFileLine[lineNum][23:42])
            SVclockDrift = float(navFileLine[lineNum][42:61])
            SVclockDriftRate = float(navFileLine[lineNum][61:80])

            IODEC = float(navFileLine[lineNum + 1][4:23])
            Crs = float(navFileLine[lineNum + 1][23:42])
            DeltaN = float(navFileLine[lineNum + 1][42:61])
            M0 = float(navFileLine[lineNum + 1][61:80])

            Cuc = float(navFileLine[lineNum + 2][4:23])
            e = float(navFileLine[lineNum + 2][23:42])
            Cus = float(navFileLine[lineNum + 2][42:61])
            sqrtA = float(navFileLine[lineNum + 2][61:80])

            toe = float(navFileLine[lineNum + 3][4:23])
            Cic = float(navFileLine[lineNum + 3][23:42])
            OMEGA0 = float(navFileLine[lineNum + 3][42:61])
            Cis = float(navFileLine[lineNum + 3][61:80])

            i0 = float(navFileLine[lineNum + 4][4:23])
            Crc = float(navFileLine[lineNum + 4][23:42])
            omega = float(navFileLine[lineNum + 4][42:61])
            OMEGA_DOT = float(navFileLine[lineNum + 4][61:80])

            IDOT = float(navFileLine[lineNum + 5][4:23])
            if navFileLine[lineNum + 5][23:42] == '                   ':
                Blank = 0.0
            else:
                Blank = float(navFileLine[lineNum + 5][23:42])
            IRN_Week = float(navFileLine[lineNum + 5][42:61])
            Spare1 = 0.0

            RangeAccuracy = float(navFileLine[lineNum + 6][4:23])
            Health = float(navFileLine[lineNum + 6][23:42])
            TGD = float(navFileLine[lineNum + 6][42:61])
            Spare2 = 0.0

            Transmission = float(navFileLine[lineNum + 7][4:23])

            lineNum += 8
            navData[sat].append(irnssNav(epoch, SVclockBias, SVclockDrift, SVclockDriftRate,
                                         IODEC, Crs, DeltaN, M0,
                                         Cuc, e, Cus, sqrtA,
                                         toe, Cic, OMEGA0, Cis,
                                         i0, Crc, omega, OMEGA_DOT,
                                         IDOT, Blank, IRN_Week, Spare1,
                                         RangeAccuracy, Health, TGD, Spare2,
                                         Transmission))
    return navData
