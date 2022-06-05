

def readPandaAtt(attFile):
    from gnssbox.module.pandaAttClass import pandaAtt
    attFileLine = open(attFile, 'r+').readlines()
    firstLine = attFileLine[0][:-1]
    beginLineIndex = attFileLine.index('%% End of header\n') + 1
    pandaAttData = []
    count = 0
    for line in attFileLine[beginLineIndex:]:
        mjd = int(line.split()[0])
        sod = float(line.split()[1])
        roll = float(line.split()[2])
        pitch = float(line.split()[3])
        yaw = float(line.split()[4])
        modeValues = float(line.split()[5])
        mode = int(line.split()[6])
        pandaAttData.append(count)
        pandaAttData[count] = pandaAtt(mjd, sod, roll, pitch, yaw, modeValues, mode)
        count += 1
    return firstLine, pandaAttData