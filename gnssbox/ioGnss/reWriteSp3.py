# Delete GNSS system from old sp3 file and output new sp3 file
def rewriteSp3File(sp3File, delSys, beginTime, endTime, outputFile=None):
    from gnssbox.ioGnss.readSp3 import readSp3Head
    if outputFile is None:
        outputFile = sp3File
    sp3Head = readSp3Head(sp3File)
    sp3FileOpen = open(sp3File, 'r+')
    sp3FileLines = sp3FileOpen.readlines()
    sp3FileOpen.close()
    sp3FileWrite = open(outputFile, 'w+')

    # write first line
    firstYear = sp3Head['epoch'][0].year
    firstMonth = sp3Head['epoch'][0].month
    firstDay = sp3Head['epoch'][0].day
    firstHour = sp3Head['epoch'][0].hour
    firstMinute = sp3Head['epoch'][0].minute
    firstSecond = sp3Head['epoch'][0].second
    firstMicrosecond = sp3Head['epoch'][0].microsecond
    firstLine = '#dP' + str(firstYear) + str(firstMonth).rjust(3) + str(firstDay).rjust(3) + str(firstHour).rjust(3) + \
                str(firstMinute).rjust(3) + str(firstSecond).rjust(3) + '.{:06d}'.format(firstMicrosecond, -6) + '00' + \
                str(sp3Head['epochNum']).rjust(8) + '   u+U' + str(sp3Head['RefSystem']).rjust(6) + ' FIT  WHU\n'
    sp3FileWrite.write(firstLine)

    # write time line
    timeLine = '##' + str(sp3Head['firstTime']['gpsWeek']).rjust(5) + str(
        '%.8f' % sp3Head['firstTime']['gpsSow']).rjust(16) + \
               str('%.8f' % sp3Head['firstTime']['interval']).rjust(15) + str(sp3Head['firstTime']['mjd']).rjust(6) + \
               str('%.13f' % sp3Head['firstTime']['sod']).rjust(16) + '\n'
    sp3FileWrite.write(timeLine)

    # PRN LIST line
    prnList = []
    prnPreList = []
    for prn in range(0, len(sp3Head['prn'])):
        if sp3Head['prn'][prn][0] not in delSys:
            prnList.append(str(sp3Head['prn'][prn]))
            prnPreList.append(sp3Head['satPre'][prn])
    prnListLen = int(len(prnList) / 17)
    LastPrnListLen = 17 - len(prnList) + int(len(prnList) / 17) * 17

    # write sat line
    for prnListLenLine in range(0, prnListLen):
        if prnListLenLine == 0:
            line = '+' + str(len(prnList)).rjust(5) + '   '
        else:
            line = '+        '
        for lineIndex in range(0, 17):
            line += prnList[prnListLenLine * 17 + lineIndex]
        sp3FileWrite.write(line + '\n')
    if LastPrnListLen > 0:
        line = '+        '
        for lineIndex in range(prnListLen * 17, len(prnList)):
            line += prnList[lineIndex]
        line += LastPrnListLen * '  0'
        sp3FileWrite.write(line + '\n')
    sp3FileWrite.write('+          0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0\n')
    sp3FileWrite.write('+          0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0\n')

    # write sat precision
    for prnListLenLine in range(0, prnListLen):
        line = '++       '
        for lineIndex in range(0, 17):
            line += str(prnPreList[prnListLenLine * 17 + lineIndex]).rjust(3)
        sp3FileWrite.write(line + '\n')
    if LastPrnListLen > 0:
        line = '++       '
        for lineIndex in range(prnListLen * 17, len(prnList)):
            line += str(prnPreList[lineIndex]).rjust(3)
        line += LastPrnListLen * '  0'
        sp3FileWrite.write(line + '\n')
    sp3FileWrite.write('++         0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0\n')
    sp3FileWrite.write('++         0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0\n')
    for cfiLine in sp3Head['cfi']:
        sp3FileWrite.write(cfiLine)
    for commentLine in sp3Head['comment']:
        sp3FileWrite.write(commentLine)
    sp3FileWrite.write('/* CHUNTAO CHANG (EMAIL:1252443496@QQ.COM) (GNSSBOX)\n')

    beginTimeLine = 0
    bgline = '*  ' + str(beginTime.year) + str(beginTime.month).rjust(3) + str(beginTime.day).rjust(3) + str(
        beginTime.hour).rjust(3)
    endTimeLine = 0
    edLine = '*  ' + str(endTime.year) + str(endTime.month).rjust(3) + str(endTime.day).rjust(3) + str(
        endTime.hour).rjust(3)
    for sp3Line in sp3FileLines:
        if sp3Line[:16] == bgline:
            break
        beginTimeLine += 1

    for sp3Line in sp3FileLines:
        if sp3Line[:16] == edLine:
            break
        endTimeLine += 1
    for sp3Line in sp3FileLines[beginTimeLine:endTimeLine - 1]:
        if sp3Line[1] not in delSys:
            sp3FileWrite.write(sp3Line)
    sp3FileWrite.write('EOF')