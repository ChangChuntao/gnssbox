#!/usr/bin/python3
# coding=utf-8
# gnssbox           : The most complete GNSS Python toolkit ever
# Github            : https://github.com/ChangChuntao/gnssbox.git
# navDif            : Broadcast ephemeris comparison
# Author            : Chang Chuntao 1252443496@qq.com
# Copyright(C)      : The GNSS Center, Wuhan University
# Creation Date     : 2022.07.14
# Latest Version    : 2022.07.14 - Version 1.00

# 2022.07.14 : 广播星历对比，并以广播星历格式输出文件
#              by ChangChuntao -> Version : 1.00
def navDif(oriNavFile, comparaNavFile, difNavFile=None):
    # oriNavFile        : 源广播星历文件
    # comparaNavFile    : 对比广播星历文件
    # difNavFile        : 输出广播星历文件(可选)
    from gnssbox.ioGnss.readNav import readNav, readNavHead
    from gnssbox.module.navClass import bdsNav, gpsNav, galileoNav, glonassNav, irnssNav, sbasNav, qzssNav
    from gnssbox.ioGnss.writeNav import writeNav
    # 输出文件的文件名
    if difNavFile is None:
        difNavFile = oriNavFile + '_' + str(comparaNavFile).split('\\')[-1][:4] + '_dif'
    # 读取源广播星历
    oriNavData = readNav(oriNavFile)
    # 读取对比广播星历
    comparaNavData = readNav(comparaNavFile)
    # 读取源广播星历文件头
    oriNavHead = readNavHead(oriNavFile)
    # 新建对比结果字典difNavData
    difNavData = {}
    # 广播星历数据格式见readNav
    # 卫星号循环
    for satPrnInOri in oriNavData:
        # 判断在对比广播星历内是否有此卫星号
        if satPrnInOri in comparaNavData:
            # 源广播星历历元循环，寻找与对比广播星历的相同历元
            for oriEpochData in oriNavData[satPrnInOri]:
                # 对比广播星历历元循环
                for comEpochData in comparaNavData[satPrnInOri]:
                    # 找到对比广播星历此历元的数据
                    if oriEpochData.Epoch == comEpochData.Epoch:
                        # 判断difNavData字典内有无此卫星值 若无则新建
                        if satPrnInOri not in difNavData:
                            difNavData[satPrnInOri] = []
                        # 若卫星为北斗时
                        if satPrnInOri[0] == 'C':
                            # 对应值做差
                            SVclockBias = oriEpochData.SVclockBias - comEpochData.SVclockBias
                            SVclockDrift = oriEpochData.SVclockDrift - comEpochData.SVclockDrift
                            SVclockDriftRate = oriEpochData.SVclockDriftRate - comEpochData.SVclockDriftRate
                            AODE = oriEpochData.AODE - comEpochData.AODE
                            Crs = oriEpochData.Crs - comEpochData.Crs
                            DeltaN = oriEpochData.DeltaN - comEpochData.DeltaN
                            M0 = oriEpochData.M0 - comEpochData.M0
                            Cuc = oriEpochData.Cuc - comEpochData.Cuc
                            e = oriEpochData.e - comEpochData.e
                            Cus = oriEpochData.Cus - comEpochData.Cus
                            sqrtA = oriEpochData.sqrtA - comEpochData.sqrtA
                            toe = oriEpochData.toe - comEpochData.toe
                            Cic = oriEpochData.Cic - comEpochData.Cic
                            OMEGA0 = oriEpochData.OMEGA0 - comEpochData.OMEGA0
                            Cis = oriEpochData.Cis - comEpochData.Cis
                            i0 = oriEpochData.i0 - comEpochData.i0
                            Crc = oriEpochData.Crc - comEpochData.Crc
                            omega = oriEpochData.omega - comEpochData.omega
                            OMEGA_DOT = oriEpochData.OMEGA_DOT - comEpochData.OMEGA_DOT
                            IDOT = oriEpochData.IDOT - comEpochData.IDOT
                            Spare1 = oriEpochData.Spare1 - comEpochData.Spare1
                            BDT_Week = oriEpochData.BDT_Week - comEpochData.BDT_Week
                            Spare2 = oriEpochData.Spare2 - comEpochData.Spare2
                            SVaccuracy = oriEpochData.SVaccuracy - comEpochData.SVaccuracy
                            SatH1 = oriEpochData.SatH1 - comEpochData.SatH1
                            TGD1 = oriEpochData.TGD1 - comEpochData.TGD1
                            TGD2 = oriEpochData.TGD2 - comEpochData.TGD2
                            Transmission = oriEpochData.Transmission - comEpochData.Transmission
                            AODC = oriEpochData.AODC - comEpochData.AODC
                            # 以bdsNav类形式储存
                            difNavData[satPrnInOri].append(
                                bdsNav(oriEpochData.Epoch, SVclockBias, SVclockDrift, SVclockDriftRate,
                                       AODE, Crs, DeltaN, M0, Cuc, e, Cus,
                                       sqrtA, toe, Cic, OMEGA0, Cis,
                                       i0, Crc, omega, OMEGA_DOT, IDOT, Spare1, BDT_Week, Spare2,
                                       SVaccuracy, SatH1, TGD1, TGD2, Transmission, AODC))
                        # 同上
                        elif satPrnInOri[0] == 'G':
                            SVclockBias = oriEpochData.SVclockBias - comEpochData.SVclockBias
                            SVclockDrift = oriEpochData.SVclockDrift - comEpochData.SVclockDrift
                            SVclockDriftRate = oriEpochData.SVclockDriftRate - comEpochData.SVclockDriftRate
                            IODE = oriEpochData.IODE - comEpochData.IODE
                            Crs = oriEpochData.Crs - comEpochData.Crs
                            DeltaN = oriEpochData.DeltaN - comEpochData.DeltaN
                            M0 = oriEpochData.M0 - comEpochData.M0
                            Cuc = oriEpochData.Cuc - comEpochData.Cuc
                            e = oriEpochData.e - comEpochData.e
                            Cus = oriEpochData.Cus - comEpochData.Cus
                            sqrtA = oriEpochData.sqrtA - comEpochData.sqrtA
                            toe = oriEpochData.toe - comEpochData.toe
                            Cic = oriEpochData.Cic - comEpochData.Cic
                            OMEGA0 = oriEpochData.OMEGA0 - comEpochData.OMEGA0
                            Cis = oriEpochData.Cis - comEpochData.Cis
                            i0 = oriEpochData.i0 - comEpochData.i0
                            Crc = oriEpochData.Crc - comEpochData.Crc
                            omega = oriEpochData.omega - comEpochData.omega
                            OMEGA_DOT = oriEpochData.OMEGA_DOT - comEpochData.OMEGA_DOT
                            IDOT = oriEpochData.IDOT - comEpochData.IDOT
                            L2Codes = oriEpochData.L2Codes - comEpochData.L2Codes
                            GPS_Week = oriEpochData.GPS_Week - comEpochData.GPS_Week
                            L2PdataFlag = oriEpochData.L2PdataFlag - comEpochData.L2PdataFlag
                            SVaccuracy = oriEpochData.SVaccuracy - comEpochData.SVaccuracy
                            SVhealth = oriEpochData.SVhealth - comEpochData.SVhealth
                            TGD = oriEpochData.TGD - comEpochData.TGD
                            IODC = oriEpochData.IODC - comEpochData.IODC
                            Transmission = oriEpochData.Transmission - comEpochData.Transmission
                            FitIntervalHours = oriEpochData.FitIntervalHours - comEpochData.FitIntervalHours
                            difNavData[satPrnInOri].append(
                                gpsNav(oriEpochData.Epoch, SVclockBias, SVclockDrift, SVclockDriftRate,
                                       IODE, Crs, DeltaN, M0, Cuc, e, Cus,
                                       sqrtA, toe, Cic, OMEGA0, Cis,
                                       i0, Crc, omega, OMEGA_DOT, IDOT, L2Codes, GPS_Week, L2PdataFlag,
                                       SVaccuracy, SVhealth, TGD, IODC, Transmission, FitIntervalHours))
                        elif satPrnInOri[0] == 'R':
                            SVclockBias = oriEpochData.SVclockBias - comEpochData.SVclockBias
                            SVrelativeFrequencyBias = oriEpochData.SVrelativeFrequencyBias - comEpochData.SVrelativeFrequencyBias
                            MessageFrameTime = oriEpochData.MessageFrameTime - comEpochData.MessageFrameTime
                            posX = oriEpochData.posX - comEpochData.posX
                            velX = oriEpochData.velX - comEpochData.velX
                            accelerationX = oriEpochData.accelerationX - comEpochData.accelerationX
                            health = oriEpochData.health - comEpochData.health
                            posY = oriEpochData.posY - comEpochData.posY
                            velY = oriEpochData.velY - comEpochData.velY
                            accelerationY = oriEpochData.accelerationY - comEpochData.accelerationY
                            frequency = oriEpochData.frequency - comEpochData.frequency
                            posZ = oriEpochData.posZ - comEpochData.posZ
                            velZ = oriEpochData.velZ - comEpochData.velZ
                            accelerationZ = oriEpochData.accelerationZ - comEpochData.accelerationZ
                            operAge = oriEpochData.operAge - comEpochData.operAge
                            if oriEpochData.StatusFlags is None or comEpochData.StatusFlags is None:
                                StatusFlags = None
                                delayDif = None
                                URAI = None
                                HealthFlags = None
                            else:
                                StatusFlags = oriEpochData.StatusFlags - comEpochData.StatusFlags
                                delayDif = oriEpochData.delayDif - comEpochData.delayDif
                                URAI = oriEpochData.URAI - comEpochData.URAI
                                HealthFlags = oriEpochData.HealthFlags - comEpochData.HealthFlags
                            difNavData[satPrnInOri].append(
                                glonassNav(oriEpochData.Epoch, SVclockBias, SVrelativeFrequencyBias, MessageFrameTime,
                                           posX, velX, accelerationX, health,
                                           posY, velY, accelerationY, frequency,
                                           posZ, velZ, accelerationZ, operAge,
                                           StatusFlags, delayDif, URAI, HealthFlags))
                        elif satPrnInOri[0] == 'E':
                            SVclockBias = oriEpochData.SVclockBias - comEpochData.SVclockBias
                            SVclockDrift = oriEpochData.SVclockDrift - comEpochData.SVclockDrift
                            SVclockDriftRate = oriEpochData.SVclockDriftRate - comEpochData.SVclockDriftRate
                            IODnav = oriEpochData.IODnav - comEpochData.IODnav
                            Crs = oriEpochData.Crs - comEpochData.Crs
                            DeltaN = oriEpochData.DeltaN - comEpochData.DeltaN
                            M0 = oriEpochData.M0 - comEpochData.M0
                            Cuc = oriEpochData.Cuc - comEpochData.Cuc
                            e = oriEpochData.e - comEpochData.e
                            Cus = oriEpochData.Cus - comEpochData.Cus
                            sqrtA = oriEpochData.sqrtA - comEpochData.sqrtA
                            toe = oriEpochData.toe - comEpochData.toe
                            Cic = oriEpochData.Cic - comEpochData.Cic
                            OMEGA0 = oriEpochData.OMEGA0 - comEpochData.OMEGA0
                            Cis = oriEpochData.Cis - comEpochData.Cis
                            i0 = oriEpochData.i0 - comEpochData.i0
                            Crc = oriEpochData.Crc - comEpochData.Crc
                            omega = oriEpochData.omega - comEpochData.omega
                            OMEGA_DOT = oriEpochData.OMEGA_DOT - comEpochData.OMEGA_DOT
                            IDOT = oriEpochData.IDOT - comEpochData.IDOT
                            DataSources = oriEpochData.DataSources - comEpochData.DataSources
                            GAL_Week = oriEpochData.GAL_Week - comEpochData.GAL_Week
                            Spare = oriEpochData.Spare - comEpochData.Spare
                            SISA = oriEpochData.SISA - comEpochData.SISA
                            SVhealth = oriEpochData.SVhealth - comEpochData.SVhealth
                            BGD_E5a_E1 = oriEpochData.BGD_E5a_E1 - comEpochData.BGD_E5a_E1
                            BGD_E5b_E1 = oriEpochData.BGD_E5b_E1 - comEpochData.BGD_E5b_E1
                            Transmission = oriEpochData.Transmission - comEpochData.Transmission
                            difNavData[satPrnInOri].append(
                                galileoNav(oriEpochData.Epoch, SVclockBias, SVclockDrift, SVclockDriftRate,
                                           IODnav, Crs, DeltaN, M0, Cuc, e, Cus,
                                           sqrtA, toe, Cic, OMEGA0, Cis,
                                           i0, Crc, omega, OMEGA_DOT, IDOT, DataSources, GAL_Week, Spare,
                                           SISA, SVhealth, BGD_E5a_E1, BGD_E5b_E1, Transmission))
                        elif satPrnInOri[0] == 'I':
                            SVclockBias = oriEpochData.SVclockBias - comEpochData.SVclockBias
                            SVclockDrift = oriEpochData.SVclockDrift - comEpochData.SVclockDrift
                            SVclockDriftRate = oriEpochData.SVclockDriftRate - comEpochData.SVclockDriftRate
                            IODEC = oriEpochData.IODEC - comEpochData.IODEC
                            Crs = oriEpochData.Crs - comEpochData.Crs
                            DeltaN = oriEpochData.DeltaN - comEpochData.DeltaN
                            M0 = oriEpochData.M0 - comEpochData.M0
                            Cuc = oriEpochData.Cuc - comEpochData.Cuc
                            e = oriEpochData.e - comEpochData.e
                            Cus = oriEpochData.Cus - comEpochData.Cus
                            sqrtA = oriEpochData.sqrtA - comEpochData.sqrtA
                            toe = oriEpochData.toe - comEpochData.toe
                            Cic = oriEpochData.Cic - comEpochData.Cic
                            OMEGA0 = oriEpochData.OMEGA0 - comEpochData.OMEGA0
                            Cis = oriEpochData.Cis - comEpochData.Cis
                            i0 = oriEpochData.i0 - comEpochData.i0
                            Crc = oriEpochData.Crc - comEpochData.Crc
                            omega = oriEpochData.omega - comEpochData.omega
                            OMEGA_DOT = oriEpochData.OMEGA_DOT - comEpochData.OMEGA_DOT
                            IDOT = oriEpochData.IDOT - comEpochData.IDOT
                            Blank = oriEpochData.Blank - comEpochData.Blank
                            IRN_Week = oriEpochData.IRN_Week - comEpochData.IRN_Week
                            Spare1 = oriEpochData.Spare1 - comEpochData.Spare1
                            RangeAccuracy = oriEpochData.RangeAccuracy - comEpochData.RangeAccuracy
                            Health = oriEpochData.Health - comEpochData.Health
                            TGD = oriEpochData.TGD - comEpochData.TGD
                            Spare2 = oriEpochData.Spare2 - comEpochData.Spare2
                            Transmission = oriEpochData.Transmission - comEpochData.Transmission
                            difNavData[satPrnInOri].append(
                                irnssNav(oriEpochData.Epoch, SVclockBias, SVclockDrift, SVclockDriftRate,
                                         IODEC, Crs, DeltaN, M0,
                                         Cuc, e, Cus, sqrtA,
                                         toe, Cic, OMEGA0, Cis,
                                         i0, Crc, omega, OMEGA_DOT,
                                         IDOT, Blank, IRN_Week, Spare1,
                                         RangeAccuracy, Health, TGD, Spare2,
                                         Transmission))
                        elif satPrnInOri[0] == 'S':
                            SVclockBias = oriEpochData.SVclockBias - comEpochData.SVclockBias
                            SVrelativeFrequencyBias = oriEpochData.SVrelativeFrequencyBias - comEpochData.SVrelativeFrequencyBias
                            Transmission = oriEpochData.Transmission - comEpochData.Transmission
                            posX = oriEpochData.posX - comEpochData.posX
                            velX = oriEpochData.velX - comEpochData.velX
                            accelerationX = oriEpochData.accelerationX - comEpochData.accelerationX
                            health = oriEpochData.health - comEpochData.health
                            posY = oriEpochData.posY - comEpochData.posY
                            velY = oriEpochData.velY - comEpochData.velY
                            accelerationY = oriEpochData.accelerationY - comEpochData.accelerationY
                            AccuracyCode = oriEpochData.AccuracyCode - comEpochData.AccuracyCode
                            posZ = oriEpochData.posZ - comEpochData.posZ
                            velZ = oriEpochData.velZ - comEpochData.velZ
                            accelerationZ = oriEpochData.accelerationZ - comEpochData.accelerationZ
                            IODN = oriEpochData.IODN - comEpochData.IODN
                            difNavData[satPrnInOri].append(
                                sbasNav(oriEpochData.Epoch, SVclockBias, SVrelativeFrequencyBias, Transmission,
                                        posX, velX, accelerationX, health,
                                        posY, velY, accelerationY, AccuracyCode,
                                        posZ, velZ, accelerationZ, IODN))
                        elif satPrnInOri[0] == 'J':
                            SVclockBias = oriEpochData.SVclockBias - comEpochData.SVclockBias
                            SVclockDrift = oriEpochData.SVclockDrift - comEpochData.SVclockDrift
                            SVclockDriftRate = oriEpochData.SVclockDriftRate - comEpochData.SVclockDriftRate
                            IODE = oriEpochData.IODE - comEpochData.IODE
                            Crs = oriEpochData.Crs - comEpochData.Crs
                            DeltaN = oriEpochData.DeltaN - comEpochData.DeltaN
                            M0 = oriEpochData.M0 - comEpochData.M0
                            Cuc = oriEpochData.Cuc - comEpochData.Cuc
                            e = oriEpochData.e - comEpochData.e
                            Cus = oriEpochData.Cus - comEpochData.Cus
                            sqrtA = oriEpochData.sqrtA - comEpochData.sqrtA
                            toe = oriEpochData.toe - comEpochData.toe
                            Cic = oriEpochData.Cic - comEpochData.Cic
                            OMEGA0 = oriEpochData.OMEGA0 - comEpochData.OMEGA0
                            Cis = oriEpochData.Cis - comEpochData.Cis
                            i0 = oriEpochData.i0 - comEpochData.i0
                            Crc = oriEpochData.Crc - comEpochData.Crc
                            omega = oriEpochData.omega - comEpochData.omega
                            OMEGA_DOT = oriEpochData.OMEGA_DOT - comEpochData.OMEGA_DOT
                            IDOT = oriEpochData.IDOT - comEpochData.IDOT
                            L2Codes = oriEpochData.L2Codes - comEpochData.L2Codes
                            GPS_Week = oriEpochData.GPS_Week - comEpochData.GPS_Week
                            L2PdataFlag = oriEpochData.L2PdataFlag - comEpochData.L2PdataFlag
                            SVaccuracy = oriEpochData.SVaccuracy - comEpochData.SVaccuracy
                            SVhealth = oriEpochData.SVhealth - comEpochData.SVhealth
                            TGD = oriEpochData.TGD - comEpochData.TGD
                            IODC = oriEpochData.IODC - comEpochData.IODC
                            Transmission = oriEpochData.Transmission - comEpochData.Transmission
                            FitIntervalFlag = oriEpochData.FitIntervalFlag - comEpochData.FitIntervalFlag
                            difNavData[satPrnInOri].append(
                                qzssNav(oriEpochData.Epoch, SVclockBias, SVclockDrift, SVclockDriftRate,
                                        IODE, Crs, DeltaN, M0, Cuc, e, Cus,
                                        sqrtA, toe, Cic, OMEGA0, Cis,
                                        i0, Crc, omega, OMEGA_DOT, IDOT, L2Codes, GPS_Week, L2PdataFlag,
                                        SVaccuracy, SVhealth, TGD, IODC, Transmission, FitIntervalFlag))
                        break
    # 写入文件
    writeNav(oriNavHead, difNavData, difNavFile, True)
