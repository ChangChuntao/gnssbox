#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# writeClk       : Write the clk file
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.27
# Latest Version : 2022.06.27 - Version 1.00

def writeClk(clkData, clkFile):
    import sys
    clkFileWrite = open(clkFile, 'w+')
    clkFileWrite.write('     3.00           C                   M                   RINEX VERSION / TYPE\n')
    clkFileWrite.write('CCLOCK              GNSSBOX @ CCT                           PGM / RUN BY / DATE \n')
    if len(clkData['sat']) == 0:
        print('无数据!')
        sys.exit()
    elif len(clkData['sat']) != 0 and len(clkData['site']) == 0:
        clkFileWrite.write('     1    AS                                                # / TYPES OF DATA   \n')
    elif len(clkData['sat']) != 0 and len(clkData['site']) != 0:
        clkFileWrite.write('     2    AR    AS                                          # / TYPES OF DATA   \n')
    clkFileWrite.write('   GPS                                                      TIME SYSTEM ID \n')
    clkFileWrite.write('WHU  GNSS RESEARCH CENTER, WUHAN UNIVERSITY, P.R.CHINA      ANALYSIS CENTER\n')
    clkFileWrite.write(str(len(clkData['sat'])).rjust(6) + '                                                      # OF SOLN SATS      \n')
    prnListLen = int(len(clkData['sat']) / 15)
    LastPrnListLen = 15 - len(clkData['sat']) + int(len(clkData['sat']) / 15) * 15
    prnList = []
    for prn in clkData['sat']:
        prnList.append(str(prn))
    
    for prnListLenLine in range(0, prnListLen):
        line = ''
        for lineIndex in range(0, 15):
            line += prnList[prnListLenLine * 15 + lineIndex] + ' '
        clkFileWrite.write(line + 'PRN LIST\n')
    line = ''
    if LastPrnListLen > 0:
        for lineIndex in range(prnListLen * 15, len(clkData['sat'])):
            line += prnList[lineIndex] + ' '
        line += LastPrnListLen * '    '
        line += 'PRN LIST\n'
        clkFileWrite.write(line)
    clkFileWrite.write('                                                            END OF HEADER     \n')
    
    datetimeList = []
    for prn in clkData['sat']:
        for prnData in clkData['sat'][prn]:
            if prnData.epoch not in datetimeList:
                datetimeList.append(prnData.epoch)
                
    for epoch in datetimeList:
        for prn in clkData['sat']:
            for prnData in clkData['sat'][prn]:
                if prnData.epoch == epoch:
                    if prnData.clkMerror == None:
                        line = 'AS ' + prn + '  ' + str(epoch.year) + ' ' + str(epoch.month).zfill(2) + ' ' + str(epoch.day).zfill(2) + ' ' + str(epoch.hour).zfill(2) + ' ' + \
                            str(epoch.minute).zfill(2) + ('%.6f' % epoch.second).rjust(10) + '  1' + ('%.12E' % prnData.clk).rjust(22)
                        
                    else:
                        line = 'AS ' + prn + '  ' + str(epoch.year) + ' ' + str(epoch.month).zfill(2) + ' ' + str(epoch.day).zfill(2) + ' ' + str(epoch.hour).zfill(2) + ' ' + \
                            str(epoch.minute).zfill(2) + ('%.6f' % epoch.second).rjust(10) + '  2' + ('%.12E' % prnData.clk).rjust(22) + ('%.12E' % prnData.clk).rjust(20)
                    clkFileWrite.write(line + '\n')
                    break