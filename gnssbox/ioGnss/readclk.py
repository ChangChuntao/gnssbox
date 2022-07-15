
def clkFileTimeLine2Datetime(line):
    import datetime
    year = int(line.split()[0])
    month = int(line.split()[1])
    day = int(line.split()[2])
    hour = int(line.split()[3])
    minute = int(line.split()[4])
    second = int(str(line.split()[5]).split('.')[0])
    microsecond = int(int(str(line.split()[5]).split('.')[-1]))
    clkDataTime = datetime.datetime(year, month, day, hour, minute, second, microsecond)
    return clkDataTime


def readClkHead(clkFile):
    clkFileOpen = open(clkFile, 'r+')
    clkFileLines = clkFileOpen.readlines()
    clkFileOpen.close()
    clkHead = {}
    clkHead['ANALYSIS CENTER'] = 'WHU  GNSS RESEARCH CENTER, WUHAN UNIVERSITY, P.R.CHINA'
    clkDataPrn = []
    clkDatetime = []
    typeOfData = []
    for line in clkFileLines:
        if line[60:-1] == 'RINEX VERSION / TYPE':
            clkHead['RINEX VERSION'] = float(line.split()[0])
        elif line[60:-1] == 'INTERVAL':
            clkHead['INTERVAL'] = float(line.split()[0])
        elif line[60:-1] == 'PGM / RUN BY / DATE':
            clkHead['PGM'] = line.split()[0]
            clkHead['RUN BY'] = 'WHU'
            clkHead['DATE'] = ''
        elif line[60:-1] == '# OF SOLN SATS':
            clkHead['SOLN SATS'] = int(line.split()[0])
        elif line[60:-1] == 'PRN LIST':
            prnLine = line[:60].split()
            for prn in prnLine:
                clkDataPrn.append(prn)
        elif line[60:-1] == '# / TYPES OF DATA':
            if 'AR' in line.split():
                typeOfData.append('AR')
            elif 'AS' in line.split():
                typeOfData.append('AS')
        elif line[:2] == 'AS':
            nowDatetime = clkFileTimeLine2Datetime(line[8:34])
            if nowDatetime not in clkDatetime:
                clkDatetime.append(nowDatetime)
    clkHead['TYPES OF DATA'] = typeOfData
    clkHead['SOLN SATS'] = clkDataPrn
    clkHead['epochList'] = clkDatetime
    return clkHead
            