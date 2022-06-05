#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# interpolation  : Interpolation of various GNSS files
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.05
# Latest Version : 2022.06.05 - Version 1.00


def interpolationPandaAtt(pandaAttFile, interval, *outPandaAttFile):
    # pandaAttFile : PANDA ATT 文件
    # interval     ：插值采样间隔
    import datetime
    from gnssbox.ioGnss.readPandaAtt import readPandaAtt
    from gnssbox.module.pandaAttClass import pandaAtt
    from scipy.interpolate import interp1d
    from gnssbox.lib.gnssTime import gnssTimesTran

    firstLine, pandaAttData = readPandaAtt(pandaAttFile)
    epochX = []
    rollY = []
    pitchY = []
    yawY = []
    modeValuesY = []
    for data in pandaAttData:
        epochX.append(data.mjd + data.sod / 86400.e0)
        rollY.append(data.roll)
        pitchY.append(data.pitch)
        yawY.append(data.yaw)
        modeValuesY.append(data.modeValues)
    firstEpoch = datetime.datetime(pandaAttData[0].Time.year,
                                   pandaAttData[0].Time.month,
                                   pandaAttData[0].Time.day,
                                   pandaAttData[0].Time.hour,
                                   pandaAttData[0].Time.minute,
                                   pandaAttData[0].Time.second)
    endEpoch = datetime.datetime(pandaAttData[-1].Time.year,
                                 pandaAttData[-1].Time.month,
                                 pandaAttData[-1].Time.day,
                                 pandaAttData[-1].Time.hour,
                                 pandaAttData[-1].Time.minute,
                                 pandaAttData[-1].Time.second)
    Epoch = []
    outEpoch = []
    nowEpoch = firstEpoch
    while nowEpoch < endEpoch:
        nowEpoch = nowEpoch + datetime.timedelta(seconds=interval)
        [nowMjd, nowSod] = gnssTimesTran(From='DATETIME', To='MJDSOD', Time=nowEpoch)
        Epoch.append(nowMjd + nowSod / 86400.e0)
        outEpoch.append([nowMjd, nowSod])

    linearRollf = interp1d(epochX, rollY, kind="linear")
    newRoll = linearRollf(Epoch)
    linearpitchf = interp1d(epochX, pitchY, kind="linear")
    newpitch = linearpitchf(Epoch)
    linearyawf = interp1d(epochX, yawY, kind="linear")
    newyaw = linearyawf(Epoch)
    linearmodeValuesf = interp1d(epochX, modeValuesY, kind="linear")
    newmodeValues = linearmodeValuesf(Epoch)

    newPandaAttData = []
    for i in range(0, len(Epoch)):
        newPandaAttData.append(i)
        newPandaAttData[i] = pandaAtt(outEpoch[i][0], outEpoch[i][1], newRoll[i], newpitch[i], newyaw[i],
                                      newmodeValues[i], pandaAttData[1].mode)
    try:
        from gnssbox.ioGnss.writePandaAtt import writePandaAtt
        writePandaAtt(firstLine, newPandaAttData, outPandaAttFile[0])
    except:
        print('不写入文件')
