def readEle(eleFile):
    import datetime
    eleFileLine = open(eleFile, 'r+').readlines()
    eleData = []
    eleTime = []
    eleSat = []
    line2 = eleFileLine[1].split()
    firstTime = datetime.datetime(int(line2[1]), int(line2[2]), int(line2[3]), int(line2[4]), int(line2[5]),
                                  int(float(line2[6])), int(int(line2[6].split('.')[-1])))
    for lineNum in range(1, int(len(eleFileLine) / 2)):
        inLineData = []
        addTime = int(float(eleFileLine[lineNum * 2].split()[0]))
        nowTime = firstTime + datetime.timedelta(seconds=addTime)
        eleTime.append(nowTime)
        inLineData.append(nowTime)
        if eleFileLine[lineNum * 2].split()[1] == '-1' and lineNum > 2:
            inLineData.append(eleData[lineNum - 2][1])
        else:
            nowSatList = eleFileLine[lineNum * 2].split()[2:]
            inLineData.append(nowSatList)
        eleSat.append(inLineData[1])
        inLineData.append(eleFileLine[lineNum * 2 + 1].split())
        eleData.append(inLineData)
    outEleData = []
    for ele in eleData:
        inEleData = []
        inEleData.append(ele[0])
        sat = []
        for i in range(0, len(ele[1])):
            sat.append([ele[1][i], float(ele[2][i])])
        inEleData.append(sat)
        outEleData.append(inEleData)
    return eleTime, eleSat, outEleData