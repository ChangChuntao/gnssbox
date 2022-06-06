#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# plotSatTrack   : Use cartopy to map the Satellite Track
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.06
# Latest Version : 2022.06.06 - Version 1.00


def plotSatTrack(sp3File, **kwargs):
    # file     ：精密星历文件
    # system   : 卫星导航系统，例如：system = ['G', 'C'], 默认值为 ['G', 'C', 'R', 'E', 'J', 'I']
    # addFeat  : 是否添加陆地海洋海岸线，例如addFeat = False, 默认addFeat = True
    # savePng  ：保存png图片，例如：savePng = r'D:\Code\gnssbox\gnssbox\plot\example\site.png'，默认为空，不保存。
    # showImg  : 是否展示图片，仅接受True 与 False的布尔型传入，例如showImg = False，默认值showImg = True
    # shwoPRN  : 是否展示PRN号，仅接受True 与 False的布尔型传入，例如shwoPRN = False，默认值shwoPRN = True
    from gnssbox.ioGnss.readSp3 import readSp3
    import sys
    sp3Data = readSp3(sp3File)
    if 'system' in kwargs:
        gnssSystem = []
        for system in kwargs['system']:
            if system in ['G', 'C', 'R', 'E', 'J', 'I', 'L', '0']:
                gnssSystem.append(system)
            else:
                print('系统不存在, 仅限于CGREJIL')
                sys.exit()
    else:
        gnssSystem = ['I', 'J', 'E', 'R', 'G', 'C', 'L', '0']

    # 是否添加陆地海洋海岸线
    if 'addFeat' in kwargs:
        addFeat = kwargs['addFeat']
    else:
        addFeat = True
    # 是否保存文件
    if 'savePng' in kwargs:
        savePng = True
        savePngPath = kwargs['savePng']
    else:
        savePng = False
        savePngPath = ''
    if 'showImg' in kwargs:
        showImg = kwargs['showImg']
        if showImg != True or showImg != False:
            print('showImg参数只接受True或False')
    else:
        showImg = True
    # 是否绘制prn
    if 'shwoPRN' in kwargs:
        shwoPRN = kwargs['shwoPRN']
        if shwoPRN != True or shwoPRN != False:
            print('shwoPRN参数只接受True或False')
    else:
        shwoPRN = True
    # 调用cartoplot绘制卫星轨道
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
    from gnssbox.coordTran.xyz2blh import xyz2blh
    import math
    # 运行配置参数总的轴（axes）正常显示正负号（minus）
    mpl.rcParams['axes.unicode_minus'] = False
    # xy轴大小
    mpl.rc('xtick', labelsize=9)
    mpl.rc('ytick', labelsize=9)
    # xy轴方向
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    # 设置画布
    fig = plt.figure(figsize=(14, 7))
    
    # 绘制全球, 经度中心线为150°
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=150))
    # 设置标题
    ax.set_title('Ground Tracks of GNSS Satellite')
    # 设置范围
    ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
    # 经度标注范围
    ax.set_xticks([0, 60, 120, 180, 240, 300, 360], crs=ccrs.PlateCarree())
    # 维度标注范围
    ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())

    if addFeat:
        # 添加陆地
        ax.add_feature(cfeature.LAND)
        # 添加海洋
        ax.add_feature(cfeature.OCEAN)
        # 添加海岸线
        ax.add_feature(cfeature.COASTLINE, linewidth=0.1)

    gnssSatColor = {'C': "red", 'G': "grey", 'R': "blue", 'E': "green", 'J': "yellow", 'I': "black", 'L': "darkblue", '0': "darkblue"}
    gnssSatLabel = {'C': True, 'G': True, 'R': True, 'E': True, 'J': True, 'I': True, 'L': True, '0': True}
    gnssSat = {'C': "BDS", 'G': "GPS", 'R': "GLONASS", 'E': "GALILEO", 'J': "QZSS", 'I': "IRNSS", 'L': "LEO", '0': "other"}
    for prn in sp3Data:
        prnTrackL = []
        prnTrackB = []
        if prn[0] in gnssSystem:
            for epoch in sp3Data[prn]:
                B, L, H = xyz2blh(epoch.x, epoch.y, epoch.z, 'WGS84')
                prnTrackL.append(math.degrees(B))
                prnTrackB.append(math.degrees(L))
            # xy轴标注大小为x-large
            if gnssSatLabel[prn[0]]:
                ax.plot(prnTrackB, prnTrackL, color=gnssSatColor[prn[0]], transform=ccrs.Geodetic(), label=gnssSat[prn[0]])
                gnssSatLabel[prn[0]] = False
            else:
                ax.plot(prnTrackB, prnTrackL, color=gnssSatColor[prn[0]], transform=ccrs.Geodetic())
            if shwoPRN:
                # 绘制站点，三角形\红色\大小7.0
                ax.plot(prnTrackB[0], prnTrackL[0], '.', color='black', mec='k', mew=0, transform=ccrs.Geodetic(),
                        ms=7.0)
                # 添加站名标注，站名向西3°，向北2°,字体大小10
                plt.text(prnTrackB[0] - 3, prnTrackL[0] + 3, prn, transform=ccrs.Geodetic(),
                        fontsize=10)

    plt.xticks(fontsize='x-large')
    plt.yticks(fontsize='x-large')
    # 经纬线格式设置
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    # 图例
    ax.legend(ncol = len(gnssSystem), loc = 'lower center')  # 显示图例
    # 是否保存文件
    if savePng:
        fig.savefig(savePngPath, bbox_inches='tight', dpi=400)
    # 是否展示图
    if showImg:
        plt.show()
