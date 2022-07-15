#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# writeNav       : Write the nav file
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.07.15
# Latest Version : 2022.07.15 - Version 1.00


# 2022.07.15 : 写入广播星历文件
#              by ChangChuntao -> Version : 1.00
def writeNav(navHead, navData, navFile, deleteZero):
    navFileWrite = open(navFile, 'w+')
    navFileWrite.write(navHead['First Line'])
    navFileWrite.write(navHead['PGM Line'])
    navFileWrite.write(str(navHead['LEAP SECONDS']).rjust(6) +
                       '                                                      LEAP SECONDS\n')
    navFileWrite.write('                                                            END OF HEADER\n')

    for sat in navData:
        for satEpochList in navData[sat]:
            if sat[0] == 'C':
                if deleteZero and satEpochList.SVclockBias == 0.0 and satEpochList.SVclockDrift == 0.0 and satEpochList.SVclockDriftRate == 0.0 \
                        and satEpochList.AODE == 0.0 and satEpochList.Crs == 0.0 and satEpochList.DeltaN == 0.0 and satEpochList.M0 == 0.0 \
                        and satEpochList.Cuc == 0.0 and satEpochList.e == 0.0 and satEpochList.Cus == 0.0 and satEpochList.sqrtA == 0.0 \
                        and satEpochList.toe == 0.0 and satEpochList.Cic == 0.0 and satEpochList.omega == 0.0 and satEpochList.OMEGA_DOT == 0.0 \
                        and satEpochList.IDOT == 0.0 and satEpochList.Spare1 == 0.0 and satEpochList.BDT_Week == 0.0 and satEpochList.Spare2 == 0.0 \
                        and satEpochList.SVaccuracy == 0.0 and satEpochList.SatH1 == 0.0 and satEpochList.TGD1 == 0.0 and satEpochList.TGD2 == 0.0 \
                        and satEpochList.Transmission == 0.0 and satEpochList.AODC == 0.0:
                    pass
                else:
                    epochLine = sat + ' ' + str(satEpochList.Epoch.year) + ' ' + \
                                '%02d' % satEpochList.Epoch.month + ' ' + \
                                '%02d' % satEpochList.Epoch.day + ' ' + \
                                '%02d' % satEpochList.Epoch.hour + ' ' + \
                                '%02d' % satEpochList.Epoch.minute + ' ' + \
                                '%02d' % satEpochList.Epoch.second + \
                                '%19.12E' % satEpochList.SVclockBias + \
                                '%19.12E' % satEpochList.SVclockDrift + \
                                '%19.12E' % satEpochList.SVclockDriftRate + '\n'
                    navLine1 = '    ' + '%19.12E' % satEpochList.AODE + \
                               '%19.12E' % satEpochList.Crs + \
                               '%19.12E' % satEpochList.DeltaN + \
                               '%19.12E' % satEpochList.M0 + '\n'
                    navLine2 = '    ' + '%19.12E' % satEpochList.Cuc + \
                               '%19.12E' % satEpochList.e + \
                               '%19.12E' % satEpochList.Cus + \
                               '%19.12E' % satEpochList.sqrtA + '\n'
                    navLine3 = '    ' + '%19.12E' % satEpochList.toe + \
                               '%19.12E' % satEpochList.Cic + \
                               '%19.12E' % satEpochList.OMEGA0 + \
                               '%19.12E' % satEpochList.Cis + '\n'
                    navLine4 = '    ' + '%19.12E' % satEpochList.i0 + \
                               '%19.12E' % satEpochList.Crc + \
                               '%19.12E' % satEpochList.omega + \
                               '%19.12E' % satEpochList.OMEGA_DOT + '\n'
                    navLine5 = '    ' + '%19.12E' % satEpochList.IDOT + \
                               '%19.12E' % satEpochList.Spare1 + \
                               '%19.12E' % satEpochList.BDT_Week + \
                               '%19.12E' % satEpochList.Spare2 + '\n'
                    navLine6 = '    ' + '%19.12E' % satEpochList.SVaccuracy + \
                               '%19.12E' % satEpochList.SatH1 + \
                               '%19.12E' % satEpochList.TGD1 + \
                               '%19.12E' % satEpochList.TGD2 + '\n'
                    navLine7 = '    ' + '%19.12E' % satEpochList.Transmission + \
                               '%19.12E' % satEpochList.AODC + '\n'
                    navFileWrite.write(epochLine)
                    navFileWrite.write(navLine1)
                    navFileWrite.write(navLine2)
                    navFileWrite.write(navLine3)
                    navFileWrite.write(navLine4)
                    navFileWrite.write(navLine5)
                    navFileWrite.write(navLine6)
                    navFileWrite.write(navLine7)
            if sat[0] == 'G':
                if deleteZero and satEpochList.SVclockBias == 0.0 and satEpochList.SVclockDrift == 0.0 and satEpochList.SVclockDriftRate == 0.0 \
                        and satEpochList.IODE == 0.0 and satEpochList.Crs == 0.0 and satEpochList.DeltaN == 0.0 and satEpochList.M0 == 0.0 \
                        and satEpochList.Cuc == 0.0 and satEpochList.e == 0.0 and satEpochList.Cus == 0.0 and satEpochList.sqrtA == 0.0 \
                        and satEpochList.toe == 0.0 and satEpochList.Cic == 0.0 and satEpochList.omega == 0.0 and satEpochList.OMEGA_DOT == 0.0 \
                        and satEpochList.IDOT == 0.0 and satEpochList.L2Codes == 0.0 and satEpochList.GPS_Week == 0.0 and satEpochList.L2PdataFlag == 0.0  \
                        and satEpochList.SVaccuracy == 0.0 and satEpochList.SVhealth == 0.0 and satEpochList.TGD == 0.0 and satEpochList.IODC == 0.0 \
                        and satEpochList.Transmission == 0.0 and satEpochList.FitIntervalHours == 0.0:
                    pass
                else:
                    epochLine = sat + ' ' + str(satEpochList.Epoch.year) + ' ' + \
                                '%02d' % satEpochList.Epoch.month + ' ' + \
                                '%02d' % satEpochList.Epoch.day + ' ' + \
                                '%02d' % satEpochList.Epoch.hour + ' ' + \
                                '%02d' % satEpochList.Epoch.minute + ' ' + \
                                '%02d' % satEpochList.Epoch.second + \
                                '%19.12E' % satEpochList.SVclockBias + \
                                '%19.12E' % satEpochList.SVclockDrift + \
                                '%19.12E' % satEpochList.SVclockDriftRate + '\n'
                    navLine1 = '    ' + '%19.12E' % satEpochList.IODE + \
                               '%19.12E' % satEpochList.Crs + \
                               '%19.12E' % satEpochList.DeltaN + \
                               '%19.12E' % satEpochList.M0 + '\n'
                    navLine2 = '    ' + '%19.12E' % satEpochList.Cuc + \
                               '%19.12E' % satEpochList.e + \
                               '%19.12E' % satEpochList.Cus + \
                               '%19.12E' % satEpochList.sqrtA + '\n'
                    navLine3 = '    ' + '%19.12E' % satEpochList.toe + \
                               '%19.12E' % satEpochList.Cic + \
                               '%19.12E' % satEpochList.OMEGA0 + \
                               '%19.12E' % satEpochList.Cis + '\n'
                    navLine4 = '    ' + '%19.12E' % satEpochList.i0 + \
                               '%19.12E' % satEpochList.Crc + \
                               '%19.12E' % satEpochList.omega + \
                               '%19.12E' % satEpochList.OMEGA_DOT + '\n'
                    navLine5 = '    ' + '%19.12E' % satEpochList.IDOT + \
                               '%19.12E' % satEpochList.L2Codes + \
                               '%19.12E' % satEpochList.GPS_Week + \
                               '%19.12E' % satEpochList.L2PdataFlag + '\n'
                    navLine6 = '    ' + '%19.12E' % satEpochList.SVaccuracy + \
                               '%19.12E' % satEpochList.SVhealth + \
                               '%19.12E' % satEpochList.TGD + \
                               '%19.12E' % satEpochList.IODC + '\n'
                    navLine7 = '    ' + '%19.12E' % satEpochList.Transmission + \
                               '%19.12E' % satEpochList.FitIntervalHours + '\n'
                    navFileWrite.write(epochLine)
                    navFileWrite.write(navLine1)
                    navFileWrite.write(navLine2)
                    navFileWrite.write(navLine3)
                    navFileWrite.write(navLine4)
                    navFileWrite.write(navLine5)
                    navFileWrite.write(navLine6)
                    navFileWrite.write(navLine7)
            if sat[0] == 'E':
                if deleteZero and satEpochList.SVclockBias == 0.0 and satEpochList.SVclockDrift == 0.0 and satEpochList.SVclockDriftRate == 0.0 \
                        and satEpochList.IODnav == 0.0 and satEpochList.Crs == 0.0 and satEpochList.DeltaN == 0.0 and satEpochList.M0 == 0.0 \
                        and satEpochList.Cuc == 0.0 and satEpochList.e == 0.0 and satEpochList.Cus == 0.0 and satEpochList.sqrtA == 0.0 \
                        and satEpochList.toe == 0.0 and satEpochList.Cic == 0.0 and satEpochList.omega == 0.0 and satEpochList.OMEGA_DOT == 0.0 \
                        and satEpochList.IDOT == 0.0 and satEpochList.DataSources == 0.0 and satEpochList.GAL_Week == 0.0 and satEpochList.Spare == 0.0  \
                        and satEpochList.SISA == 0.0 and satEpochList.SVhealth == 0.0 and satEpochList.BGD_E5a_E1 == 0.0 and satEpochList.BGD_E5b_E1 == 0.0 \
                        and satEpochList.Transmission == 0.0:
                    pass
                else:
                    epochLine = sat + ' ' + str(satEpochList.Epoch.year) + ' ' + \
                                '%02d' % satEpochList.Epoch.month + ' ' + \
                                '%02d' % satEpochList.Epoch.day + ' ' + \
                                '%02d' % satEpochList.Epoch.hour + ' ' + \
                                '%02d' % satEpochList.Epoch.minute + ' ' + \
                                '%02d' % satEpochList.Epoch.second + \
                                '%19.12E' % satEpochList.SVclockBias + \
                                '%19.12E' % satEpochList.SVclockDrift + \
                                '%19.12E' % satEpochList.SVclockDriftRate + '\n'
                    navLine1 = '    ' + '%19.12E' % satEpochList.IODnav + \
                               '%19.12E' % satEpochList.Crs + \
                               '%19.12E' % satEpochList.DeltaN + \
                               '%19.12E' % satEpochList.M0 + '\n'
                    navLine2 = '    ' + '%19.12E' % satEpochList.Cuc + \
                               '%19.12E' % satEpochList.e + \
                               '%19.12E' % satEpochList.Cus + \
                               '%19.12E' % satEpochList.sqrtA + '\n'
                    navLine3 = '    ' + '%19.12E' % satEpochList.toe + \
                               '%19.12E' % satEpochList.Cic + \
                               '%19.12E' % satEpochList.OMEGA0 + \
                               '%19.12E' % satEpochList.Cis + '\n'
                    navLine4 = '    ' + '%19.12E' % satEpochList.i0 + \
                               '%19.12E' % satEpochList.Crc + \
                               '%19.12E' % satEpochList.omega + \
                               '%19.12E' % satEpochList.OMEGA_DOT + '\n'
                    navLine5 = '    ' + '%19.12E' % satEpochList.IDOT + \
                               '%19.12E' % satEpochList.DataSources + \
                               '%19.12E' % satEpochList.GAL_Week + \
                               '%19.12E' % satEpochList.Spare + '\n'
                    navLine6 = '    ' + '%19.12E' % satEpochList.SISA + \
                               '%19.12E' % satEpochList.SVhealth + \
                               '%19.12E' % satEpochList.BGD_E5a_E1 + \
                               '%19.12E' % satEpochList.BGD_E5b_E1 + '\n'
                    navLine7 = '    ' + '%19.12E' % satEpochList.Transmission + '\n'
                    navFileWrite.write(epochLine)
                    navFileWrite.write(navLine1)
                    navFileWrite.write(navLine2)
                    navFileWrite.write(navLine3)
                    navFileWrite.write(navLine4)
                    navFileWrite.write(navLine5)
                    navFileWrite.write(navLine6)
                    navFileWrite.write(navLine7)
            if sat[0] == 'R':
                if deleteZero and satEpochList.SVclockBias == 0.0 and satEpochList.SVrelativeFrequencyBias == 0.0 and satEpochList.MessageFrameTime == 0.0 \
                        and satEpochList.posX == 0.0 and satEpochList.velX == 0.0 and satEpochList.accelerationX == 0.0 and satEpochList.health == 0.0 \
                        and satEpochList.posY == 0.0 and satEpochList.velY == 0.0 and satEpochList.accelerationY == 0.0 and satEpochList.frequency == 0.0 \
                        and satEpochList.posZ == 0.0 and satEpochList.velZ == 0.0 and satEpochList.accelerationZ == 0.0 and satEpochList.operAge == 0.0 \
                        and satEpochList.StatusFlags == 0.0 and satEpochList.delayDif == 0.0 and satEpochList.URAI == 0.0 and satEpochList.HealthFlags == 0.0:
                    pass
                else:
                    epochLine = sat + ' ' + str(satEpochList.Epoch.year) + ' ' + \
                                '%02d' % satEpochList.Epoch.month + ' ' + \
                                '%02d' % satEpochList.Epoch.day + ' ' + \
                                '%02d' % satEpochList.Epoch.hour + ' ' + \
                                '%02d' % satEpochList.Epoch.minute + ' ' + \
                                '%02d' % satEpochList.Epoch.second + \
                                '%19.12E' % satEpochList.SVclockBias + \
                                '%19.12E' % satEpochList.SVrelativeFrequencyBias + \
                                '%19.12E' % satEpochList.MessageFrameTime + '\n'
                    navLine1 = '    ' + '%19.12E' % satEpochList.posX + \
                               '%19.12E' % satEpochList.velX + \
                               '%19.12E' % satEpochList.accelerationX + \
                               '%19.12E' % satEpochList.health + '\n'
                    navLine2 = '    ' + '%19.12E' % satEpochList.posY + \
                               '%19.12E' % satEpochList.velY + \
                               '%19.12E' % satEpochList.accelerationY + \
                               '%19.12E' % satEpochList.frequency + '\n'
                    navLine3 = '    ' + '%19.12E' % satEpochList.posZ + \
                               '%19.12E' % satEpochList.velZ + \
                               '%19.12E' % satEpochList.accelerationZ + \
                               '%19.12E' % satEpochList.operAge + '\n'
                    navLine4 = '    ' + '%19.12E' % satEpochList.StatusFlags + \
                               '%19.12E' % satEpochList.delayDif + \
                               '%19.12E' % satEpochList.URAI + \
                               '%19.12E' % satEpochList.HealthFlags + '\n'
                    navFileWrite.write(epochLine)
                    navFileWrite.write(navLine1)
                    navFileWrite.write(navLine2)
                    navFileWrite.write(navLine3)
                    if navHead['RINEX VERSION'] > 3.04:
                        navFileWrite.write(navLine4)
            if sat[0] == 'J':
                if deleteZero and satEpochList.SVclockBias == 0.0 and satEpochList.SVclockDrift == 0.0 and satEpochList.SVclockDriftRate == 0.0 \
                        and satEpochList.IODE == 0.0 and satEpochList.Crs == 0.0 and satEpochList.DeltaN == 0.0 and satEpochList.M0 == 0.0 \
                        and satEpochList.Cuc == 0.0 and satEpochList.e == 0.0 and satEpochList.Cus == 0.0 and satEpochList.sqrtA == 0.0 \
                        and satEpochList.toe == 0.0 and satEpochList.Cic == 0.0 and satEpochList.omega == 0.0 and satEpochList.OMEGA_DOT == 0.0 \
                        and satEpochList.IDOT == 0.0 and satEpochList.L2Codes == 0.0 and satEpochList.GPS_Week == 0.0 and satEpochList.L2PdataFlag == 0.0  \
                        and satEpochList.SVaccuracy == 0.0 and satEpochList.SVhealth == 0.0 and satEpochList.TGD == 0.0 and satEpochList.IODC == 0.0 \
                        and satEpochList.Transmission == 0.0 and satEpochList.FitIntervalFlag == 0.0:
                    pass
                else:
                    epochLine = sat + ' ' + str(satEpochList.Epoch.year) + ' ' + \
                                '%02d' % satEpochList.Epoch.month + ' ' + \
                                '%02d' % satEpochList.Epoch.day + ' ' + \
                                '%02d' % satEpochList.Epoch.hour + ' ' + \
                                '%02d' % satEpochList.Epoch.minute + ' ' + \
                                '%02d' % satEpochList.Epoch.second + \
                                '%19.12E' % satEpochList.SVclockBias + \
                                '%19.12E' % satEpochList.SVclockDrift + \
                                '%19.12E' % satEpochList.SVclockDriftRate + '\n'
                    navLine1 = '    ' + '%19.12E' % satEpochList.IODE + \
                               '%19.12E' % satEpochList.Crs + \
                               '%19.12E' % satEpochList.DeltaN + \
                               '%19.12E' % satEpochList.M0 + '\n'
                    navLine2 = '    ' + '%19.12E' % satEpochList.Cuc + \
                               '%19.12E' % satEpochList.e + \
                               '%19.12E' % satEpochList.Cus + \
                               '%19.12E' % satEpochList.sqrtA + '\n'
                    navLine3 = '    ' + '%19.12E' % satEpochList.toe + \
                               '%19.12E' % satEpochList.Cic + \
                               '%19.12E' % satEpochList.OMEGA0 + \
                               '%19.12E' % satEpochList.Cis + '\n'
                    navLine4 = '    ' + '%19.12E' % satEpochList.i0 + \
                               '%19.12E' % satEpochList.Crc + \
                               '%19.12E' % satEpochList.omega + \
                               '%19.12E' % satEpochList.OMEGA_DOT + '\n'
                    navLine5 = '    ' + '%19.12E' % satEpochList.IDOT + \
                               '%19.12E' % satEpochList.L2Codes + \
                               '%19.12E' % satEpochList.GPS_Week + \
                               '%19.12E' % satEpochList.L2PdataFlag + '\n'
                    navLine6 = '    ' + '%19.12E' % satEpochList.SVaccuracy + \
                               '%19.12E' % satEpochList.SVhealth + \
                               '%19.12E' % satEpochList.TGD + \
                               '%19.12E' % satEpochList.IODC + '\n'
                    navLine7 = '    ' + '%19.12E' % satEpochList.Transmission + \
                               '%19.12E' % satEpochList.FitIntervalFlag + '\n'
                    navFileWrite.write(epochLine)
                    navFileWrite.write(navLine1)
                    navFileWrite.write(navLine2)
                    navFileWrite.write(navLine3)
                    navFileWrite.write(navLine4)
                    navFileWrite.write(navLine5)
                    navFileWrite.write(navLine6)
                    navFileWrite.write(navLine7)
            if sat[0] == 'S':
                if deleteZero and satEpochList.SVclockBias == 0.0 and satEpochList.SVrelativeFrequencyBias == 0.0 and satEpochList.Transmission == 0.0 \
                        and satEpochList.posX == 0.0 and satEpochList.velX == 0.0 and satEpochList.accelerationX == 0.0 and satEpochList.health == 0.0 \
                        and satEpochList.posY == 0.0 and satEpochList.velY == 0.0 and satEpochList.accelerationY == 0.0 and satEpochList.AccuracyCode == 0.0 \
                        and satEpochList.posZ == 0.0 and satEpochList.velZ == 0.0 and satEpochList.accelerationZ == 0.0 and satEpochList.IODN == 0.0:
                    pass
                else:
                    epochLine = sat + ' ' + str(satEpochList.Epoch.year) + ' ' + \
                                '%02d' % satEpochList.Epoch.month + ' ' + \
                                '%02d' % satEpochList.Epoch.day + ' ' + \
                                '%02d' % satEpochList.Epoch.hour + ' ' + \
                                '%02d' % satEpochList.Epoch.minute + ' ' + \
                                '%02d' % satEpochList.Epoch.second + \
                                '%19.12E' % satEpochList.SVclockBias + \
                                '%19.12E' % satEpochList.SVrelativeFrequencyBias + \
                                '%19.12E' % satEpochList.Transmission + '\n'
                    navLine1 = '    ' + '%19.12E' % satEpochList.posX + \
                               '%19.12E' % satEpochList.velX + \
                               '%19.12E' % satEpochList.accelerationX + \
                               '%19.12E' % satEpochList.health + '\n'
                    navLine2 = '    ' + '%19.12E' % satEpochList.posY + \
                               '%19.12E' % satEpochList.velY + \
                               '%19.12E' % satEpochList.accelerationY + \
                               '%19.12E' % satEpochList.AccuracyCode + '\n'
                    navLine3 = '    ' + '%19.12E' % satEpochList.posZ + \
                               '%19.12E' % satEpochList.velZ + \
                               '%19.12E' % satEpochList.accelerationZ + \
                               '%19.12E' % satEpochList.IODN + '\n'
                    navFileWrite.write(epochLine)
                    navFileWrite.write(navLine1)
                    navFileWrite.write(navLine2)
                    navFileWrite.write(navLine3)
            if sat[0] == 'I':
                if deleteZero and satEpochList.SVclockBias == 0.0 and satEpochList.SVclockDrift == 0.0 and satEpochList.SVclockDriftRate == 0.0 \
                        and satEpochList.IODEC == 0.0 and satEpochList.Crs == 0.0 and satEpochList.DeltaN == 0.0 and satEpochList.M0 == 0.0 \
                        and satEpochList.Cuc == 0.0 and satEpochList.e == 0.0 and satEpochList.Cus == 0.0 and satEpochList.sqrtA == 0.0 \
                        and satEpochList.toe == 0.0 and satEpochList.Cic == 0.0 and satEpochList.omega == 0.0 and satEpochList.OMEGA_DOT == 0.0 \
                        and satEpochList.IDOT == 0.0 and satEpochList.Blank == 0.0 and satEpochList.IRN_Week == 0.0 and satEpochList.Spare1 == 0.0  \
                        and satEpochList.RangeAccuracy == 0.0 and satEpochList.Health == 0.0 and satEpochList.TGD == 0.0 and satEpochList.Spare2 == 0.0 \
                        and satEpochList.Transmission == 0.0:
                    pass
                else:
                    epochLine = sat + ' ' + str(satEpochList.Epoch.year) + ' ' + \
                                '%02d' % satEpochList.Epoch.month + ' ' + \
                                '%02d' % satEpochList.Epoch.day + ' ' + \
                                '%02d' % satEpochList.Epoch.hour + ' ' + \
                                '%02d' % satEpochList.Epoch.minute + ' ' + \
                                '%02d' % satEpochList.Epoch.second + \
                                '%19.12E' % satEpochList.SVclockBias + \
                                '%19.12E' % satEpochList.SVclockDrift + \
                                '%19.12E' % satEpochList.SVclockDriftRate + '\n'
                    navLine1 = '    ' + '%19.12E' % satEpochList.IODEC + \
                               '%19.12E' % satEpochList.Crs + \
                               '%19.12E' % satEpochList.DeltaN + \
                               '%19.12E' % satEpochList.M0 + '\n'
                    navLine2 = '    ' + '%19.12E' % satEpochList.Cuc + \
                               '%19.12E' % satEpochList.e + \
                               '%19.12E' % satEpochList.Cus + \
                               '%19.12E' % satEpochList.sqrtA + '\n'
                    navLine3 = '    ' + '%19.12E' % satEpochList.toe + \
                               '%19.12E' % satEpochList.Cic + \
                               '%19.12E' % satEpochList.OMEGA0 + \
                               '%19.12E' % satEpochList.Cis + '\n'
                    navLine4 = '    ' + '%19.12E' % satEpochList.i0 + \
                               '%19.12E' % satEpochList.Crc + \
                               '%19.12E' % satEpochList.omega + \
                               '%19.12E' % satEpochList.OMEGA_DOT + '\n'
                    navLine5 = '    ' + '%19.12E' % satEpochList.IDOT + \
                               '%19.12E' % satEpochList.Blank + \
                               '%19.12E' % satEpochList.IRN_Week + \
                               '%19.12E' % satEpochList.Spare1 + '\n'
                    navLine6 = '    ' + '%19.12E' % satEpochList.RangeAccuracy + \
                               '%19.12E' % satEpochList.Health + \
                               '%19.12E' % satEpochList.TGD + \
                               '%19.12E' % satEpochList.Spare2 + '\n'
                    navLine7 = '    ' + '%19.12E' % satEpochList.Transmission + '\n'
                    navFileWrite.write(epochLine)
                    navFileWrite.write(navLine1)
                    navFileWrite.write(navLine2)
                    navFileWrite.write(navLine3)
                    navFileWrite.write(navLine4)
                    navFileWrite.write(navLine5)
                    navFileWrite.write(navLine6)
                    navFileWrite.write(navLine7)
