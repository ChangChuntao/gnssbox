#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# plotSky        : Use cartopy to map the Satellite sky map
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.03
# Latest Version : 2022.06.03 - Version 1.00


# 2022.06.03 : 读取参数，绘制卫星天空图
#              by ChangChuntao -> Version : 1.00
def plotSatSky(**kwargs):
    # datetime\coord为必选参数，除sp3File其他为可选参数
    # datetime ：时间参数，datetime = datetime(2022,1,10,0,15,0) ,为datetime类型
    # sp3File  ：精密星历文件,例如：sp3File = 'D:\Code\gnssbox\gnssbox\ioGnss\Example\wum21921.sp3'
    # coord    ：站点位置[x, y, z],例如：coord = [-2.14874458e+06, 4.42664117e+06, 4.04465581e+06]
    # system   : 卫星导航系统，例如：system = ['G', 'C'], 默认值为 system = ['G', 'C', 'R', 'E', 'J', 'I']
    import sys
    import math
    from gnssbox.ioGnss.readSp3 import readSp3
    from gnssbox.ioGnss.readBrdc import readBrdc
    from gnssbox.coordTran.sat2siteAngle import sat2siteAngle
    from matplotlib import pyplot as plt
    print(kwargs)
    # 获取绘制时间为plotTime
    if 'datetime' in kwargs:
        plotTime = kwargs['datetime']
    else:
        print('datetime时间参数未传入')
        sys.exit()
    # 获取站点位置
    if 'coord' in kwargs:
        coord = kwargs['coord']
    else:
        print('站点位置xyz未被指定!')
        sys.exit()
    # 获取精密星历或广播星历
    if 'sp3File' in kwargs:
        sp3Data = readSp3(kwargs['sp3File'])
    else:
        print('参数未被正确指定')
        sys.exit()
    # 导航系统选择
    if 'system' in kwargs:
        gnssSystem = []
        for system in kwargs['system']:
            if system in ['G', 'C', 'R', 'E', 'J', 'I']:
                gnssSystem.append(system)
            else:
                print('系统不存在, 仅限于CGREJI')
                sys.exit()
    else:
        gnssSystem = ['I', 'J', 'E', 'R', 'G', 'C']

    plt.figure(figsize=(7, 7))
    ax = plt.subplot(111, projection='polar')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    labels = ['N', '45°', 'E', '135°', 'S', '225°', 'W', '315°']
    ax.set_thetagrids(range(0, 360, 45), labels, fontweight='semibold')
    satAzi = [0, 0, 0, 0, 0, 0]  # 卫星的空天图和极径方向正好相反，所以刻度值是自己画的
    satEle = [0, 15, 30, 45, 60, 75]
    satDegree = ['90', '75', '60', '45', '30', '15']
    c = ax.scatter(satAzi, satEle, marker=".", alpha=0.75)  # 用来画散点图，marker-->控制点的形状， alpha-->控制透明度（0-1）
    for i in range(0, 6):
        ax.text(satAzi[i], satEle[i], satDegree[i])
    ax.set_theta_direction(-1)

    gnssSatColor = {'C': "red", 'G': "grey", 'R': "blue", 'E': "green", 'J': "yellow", 'I': "black"}
    # 
    if 'sp3File' in kwargs:
        for prn in sp3Data:
            if prn[0] in gnssSystem:
                for epoch in sp3Data[prn]:
                    if epoch.epoch > plotTime or epoch.epoch == plotTime:
                        Zenith, Azi, Ele = sat2siteAngle(epoch.x, epoch.y, epoch.z, coord[0], coord[1], coord[2])
                        if Ele > math.radians(10.0):
                            plt.annotate(prn, xy=(Azi, Zenith), xycoords="data",
                                         va="center", ha="center", fontsize=8,
                                         bbox=dict(boxstyle="circle", fc=gnssSatColor[prn[0]]))
                        break
    ax.set_rlim(0, math.pi / 2)
    plt.show()
