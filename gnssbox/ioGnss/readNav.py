
def readNav(navigationFile):
    from gnssbox.module.navClass import Navigation
    import datetime
    import numpy as np
    import pandas as pd
    """
    读取导航电文
    :param navigationFile:
    :return:
    """
    f = open(navigationFile)
    nav = f.readlines()
    line = 0
    version = None # 版本
    alphaList = None # ION ALPHA
    betaList = None # ION BETA
    while True:
        if 'RINEX VERSION / TYPE' in nav[line]:
            version = nav[line][0:-21].split()[0]
            line += 1
        if 'ION ALPHA' in nav[line]:
            alphaList = nav[line][0:55].split()
            line += 1
        if 'ION BETA' in nav[line]:
            betaList = nav[line][0:55].split()
            line += 1
        elif 'END OF HEADER' in nav[line]:
            line += 1
            break
        else:
            line += 1
    del nav[0:line]
    nav = [lines.replace('D', 'E') for lines in nav]
    nav = [lines.replace('E ', 'E0') for lines in nav]
    nav = [lines.replace('0-', '0 -') for lines in nav]
    nav = [lines.replace('1-', '1 -') for lines in nav]
    nav = [lines.replace('2-', '2 -') for lines in nav]
    nav = [lines.replace('3-', '3 -') for lines in nav]
    nav = [lines.replace('4-', '4 -') for lines in nav]
    nav = [lines.replace('5-', '5 -') for lines in nav]
    nav = [lines.replace('6-', '6 -') for lines in nav]
    nav = [lines.replace('7-', '7 -') for lines in nav]
    nav = [lines.replace('8-', '8 -') for lines in nav]
    nav = [lines.replace('9-', '9 -') for lines in nav]
    nav = [lines.split() for lines in nav]
    ephemeris_list = []
    svList = []
    PRN_old = "X00"
    epoch_old = datetime.datetime.now()
    while True:
        # --------------------------------------------------------------
        GPS = GLONASS = GALILEO = COMPASS = SBAS = False
        PRN = nav[0][0]
        if "G" in PRN:
            GPS = True
        elif "R" in PRN:
            GLONASS = True
        elif "E" in PRN:
            GALILEO = True
        elif "C" in PRN:
            COMPASS = True
        elif "J" in PRN:
            QZSS = True
        elif "I" in PRN:
            IRSS = True
        elif "S" in PRN:
            SBAS = True
        else:
            if len(PRN) == 1:
                PRN = 'G0' + PRN
            elif len(PRN) == 2:
                PRN = 'G' + PRN

        if len(nav[0][1]) == 2:
            year = int(nav[0][1])
            if 79 < year < 100:
                year += 1900
            elif year <= 79:
                year += 2000
            else:
                # 自动触发异常
                raise Warning('Navigation year is not recognized! | Program stopped!')
        else:
            year = int(nav[0][1])
        month, day, hour, minute, second = int(nav[0][2]), int(nav[0][3]), int(nav[0][4]), int(nav[0][5]), int(float(nav[0][6]))
        epoch = datetime.datetime(year=year,
                                  month=month,
                                  day=day,
                                  hour=hour,
                                  minute=minute,
                                  second=second)
        # --------------------------------------------------------------
        clockBias = nav[0][7]
        clockDrift = nav[0][8]
        clockDriftRate = nav[0][9]
        if GLONASS or SBAS:
            x, vx, ax = float(nav[1][0]), float(nav[1][1]), float(nav[1][2])
            y, vy, ay = float(nav[2][0]), float(nav[2][1]), float(nav[2][2])
            z, vz, az = float(nav[3][0]), float(nav[3][1]), float(nav[3][2])
            health = float(nav[1][3])
            freqNumber = float(nav[2][3])
            operationDay = float(nav[3][3])
            sqrtA, toe, m0, e, delta_n, smallomega, cus, cuc, crs, crc, cis, cic, idot, i0, bigomega0, bigomegadot = [np.nan for _ in range(16)]
            if PRN == PRN_old and epoch == epoch_old:
                ephemeris_list[-1] = [PRN, epoch, clockBias, clockDrift,
                                      clockDriftRate, sqrtA, toe, m0, e, delta_n,
                                      smallomega, cus, cuc, crs, crc, cis, cic,
                                      idot, i0, bigomega0, bigomegadot,
                                      x, y, z, vx, vy, vz, ax, ay, az,
                                      health, freqNumber, operationDay]
            else:
                svList.append(PRN)
                ephemeris_list.append([PRN, epoch, clockBias, clockDrift,
                                       clockDriftRate, sqrtA, toe, m0, e, delta_n,
                                       smallomega, cus, cuc, crs, crc, cis, cic,
                                       idot, i0, bigomega0, bigomegadot,
                                       x, y, z, vx, vy, vz, ax, ay, az,
                                       health, freqNumber, operationDay])
            del nav[0:4]
        else:
            e = float(nav[2][1])
            m0 = float(nav[1][3])
            i0 = float(nav[4][0])
            toe = float(nav[3][0])
            cus = float(nav[2][2])
            cuc = float(nav[2][0])
            crs = float(nav[1][1])
            crc = float(nav[4][1])
            cis = float(nav[3][3])
            cic = float(nav[3][1])
            idot = float(nav[5][0])
            sqrtA = float(nav[2][3])
            delta_n = float(nav[1][2])
            smallomega = float(nav[4][2])
            bigomega0 = float(nav[3][2])
            bigomegadot = float(nav[4][3])
            x, y, z, vx, vy, vz, ax, ay, az, health, freqNumber, operationDay = [np.nan for _ in range(12)]
            if PRN == PRN_old and epoch == epoch_old:
                ephemeris_list[-1] = [PRN, epoch, clockBias, clockDrift,
                                      clockDriftRate, sqrtA, toe, m0, e, delta_n,
                                      smallomega, cus, cuc, crs, crc, cis, cic,
                                      idot, i0, bigomega0, bigomegadot,
                                      x, y, z, vx, vy, vz, ax, ay, az,
                                      health, freqNumber, operationDay]
            else:
                svList.append(PRN)
                ephemeris_list.append([PRN, epoch, clockBias, clockDrift,
                                       clockDriftRate, sqrtA, toe, m0, e, delta_n,
                                       smallomega, cus, cuc, crs, crc, cis, cic,
                                       idot, i0, bigomega0, bigomegadot,
                                       x, y, z, vx, vy, vz, ax, ay, az,
                                       health, freqNumber, operationDay])
            del nav[0:8]
        PRN_old = PRN
        epoch_old = epoch
        if len(nav) == 0:
            break
    columnNames = ["SV", "Epoch", "clockBias", "clockDrift", "clockDriftRate", "sqrtA", "toe", "m0", "eccentricity",
                   "delta_n","smallomega", "cus", "cuc", "crs", "crc", "cis", "cic",
                   "idot", "i0", "bigomega0", "bigomegadot",
                   "x", "y", "z", "vx", "vy", "vz", "ax", "ay", "az",
                   "health", "freqNumber", "operationDay"]
    ephemeris = pd.DataFrame(ephemeris_list, index=svList, columns=columnNames)
    ephemeris.index.name = 'SV'
    ephemeris["epoch"] = ephemeris.Epoch
    ephemeris.set_index('Epoch', append=True, inplace=True)
    ephemeris = ephemeris.reorder_levels(['Epoch', 'SV'])
    ephemeris = ephemeris.drop(["SV"], axis=1)

    fileEpoch = datetime.date(year=year,
                              month=month,
                              day=day)
    f.close()  # close the file
    return Navigation(fileEpoch, ephemeris, version, alphaList, betaList)


readNav(r'D:\Code\gnssbox\gnssbox\ioGnss\Example\brdm0010.22p')