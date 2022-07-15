def readSn(SnFile):
    import datetime
    SnFileLine = open(SnFile, 'r+').readlines()
    SnData = []
    SnTime = []
    SnSat = []
    line2 = SnFileLine[1].split()
    firstTime = datetime.datetime(int(line2[1]), int(line2[2]), int(line2[3]), int(line2[4]), int(line2[5]),
                                  int(float(line2[6])), int(int(line2[6].split('.')[-1])))
    for lineNum in range(1, int(len(SnFileLine) / 2)):
        inLineData = []
        addTime = int(float(SnFileLine[lineNum * 2].split()[0]))
        nowTime = firstTime + datetime.timedelta(seconds=addTime)
        SnTime.append(nowTime)
        inLineData.append(nowTime)
        if SnFileLine[lineNum * 2].split()[1] == '-1' and lineNum > 2:
            inLineData.append(SnData[lineNum - 2][1])
        else:
            nowSatList = SnFileLine[lineNum * 2].split()[2:]
            inLineData.append(nowSatList)
        SnSat.append(inLineData[1])
        inLineData.append(SnFileLine[lineNum * 2 + 1].split())
        SnData.append(inLineData)
    outSnData = []
    for Sn in SnData:
        inSnData = [Sn[0]]
        sat = []
        for i in range(0, len(Sn[1])):
            sat.append([Sn[1][i], float(Sn[2][i])])
        inSnData.append(sat)
        outSnData.append(inSnData)
    return SnTime, SnSat, outSnData
    