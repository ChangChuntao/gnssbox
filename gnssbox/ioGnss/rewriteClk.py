# Delete GNSS system from old clk file and output new clk file
def rewriteClkFile(clkFile, delSys, startDelTime, endDelTime, outputFile=None):
    from gnssbox.ioGnss.readclk import readClkHead, clkFileTimeLine2Datetime
    if outputFile is None:
        outputFile = clkFile
    clkFileOpen = open(clkFile, 'r+')
    clkFileLines = clkFileOpen.readlines()
    clkFileOpen.close()
    clkHead = readClkHead(clkFile)
    beforeDelSatList = clkHead['SOLN SATS']
    afterDelSatList = []
    for satPrn in beforeDelSatList:
        if satPrn[0] not in delSys:
            afterDelSatList.append(satPrn)
    clkHead['SOLN SATS'] = afterDelSatList
    # 文件写入
    clkFileWrite = open(outputFile, 'w+')

    # 写入头文件
    # 版本号，类型
    clkFileWrite.write('     ' + '%.2f' % clkHead[
        'RINEX VERSION'] + '           C                   M                   RINEX VERSION / TYPE\n')
    # 内容，组织
    clkFileWrite.write(
        str('PANDA-MEGCLK').ljust(20) + str('WHU').ljust(20) + '                    PGM / RUN BY / DATE\n')
    # 判断钟差写入类型
    clkFileWrite.write('     1    AS                                                # / TYPES OF DATA\n')
    # 时间格式
    clkFileWrite.write('   GPS                                                      TIME SYSTEM ID\n')
    # 'INTERVAL'
    if clkHead['INTERVAL'] is not None:
        clkFileWrite.write(str('%.2f' % clkHead['INTERVAL']).rjust(
            9) + '                                                   INTERVAL\n')
    # 组织单位
    clkFileWrite.write(str(clkHead['ANALYSIS CENTER']).ljust(60) + 'ANALYSIS CENTER\n')
    # 卫星数量
    clkFileWrite.write(str(len(clkHead['SOLN SATS'])).rjust(
        6) + '                                                      # OF SOLN SATS\n')
    # PRN LIST
    prnListLen = int(len(clkHead['SOLN SATS']) / 15)
    LastPrnListLen = 15 - len(clkHead['SOLN SATS']) + int(len(clkHead['SOLN SATS']) / 15) * 15
    prnList = []
    for prn in clkHead['SOLN SATS']:
        prnList.append(str(prn))

    for prnListLenLine in range(0, prnListLen):
        line = ''
        for lineIndex in range(0, 15):
            line += prnList[prnListLenLine * 15 + lineIndex] + ' '
        clkFileWrite.write(line + 'PRN LIST\n')
    line = ''
    if LastPrnListLen > 0:
        for lineIndex in range(prnListLen * 15, len(clkHead['SOLN SATS'])):
            line += prnList[lineIndex] + ' '
        line += LastPrnListLen * '    '
        line += 'PRN LIST\n'
        clkFileWrite.write(line)
    # 文件头写入完成
    clkFileWrite.write('                                                            END OF HEADER\n')
    for clkLine in clkFileLines:

        if clkLine[:3] == 'AS ':
            if clkLine[3] not in delSys:
                nowDatetime = clkFileTimeLine2Datetime(clkLine[8:34])
                if startDelTime <= nowDatetime < endDelTime:
                    clkFileWrite.write(clkLine)