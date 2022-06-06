#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# plotSite       : Use cartopy to map the site
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.03
# Latest Version : 2022.06.03 - Version 1.00


# 2022.06.03 : 读取参数，调用cartoplot函数绘制站点
#              by ChangChuntao -> Version : 1.00
def plotSite(**kwargs):
    from gnssbox.ioGnss.readsiteinfo import readsiteinfo
    import sys
    # 传入可选参数，除file\site\igssite必须传入其中之一，其他项都为可选选项
    # file   ：站点信息文件,例如：file=r"D:\Code\gnssbox\gnssbox\plot\example\site.info"
    # site   ：站点信息,例如：site = {'JOZE': {'L': 21.03139, 'B': 52.09722}, 'TIXI': {'L': 128.86639, 'B': 71.63444}}
    # igssite: igs站点名，例如：igssite = ['bjfs', 'irkj', 'urum', 'abpo', 'joze', 'tixi']
    # autoLB : 自动确定绘图范围，例如：autoLB = True, 默认autoLB = False
    #          autoLB 为 True时，L\B 不可同时传入
    # L      : 经度范围，例如：L = [  0, 270]，默认值L = [-180, 180]
    # B      : 纬度范围，例如：B = [-60,  60]，默认值B = [ -90,  90]
    # addFeat: 是否添加陆地海洋海岸线，例如addFeat = False, 默认addFeat = True
    # savePng：保存png图片，例如：savePng = r'D:\Code\gnssbox\gnssbox\plot\example\site.png'，默认为空，不保存。
    # showImg: 是否展示图片，仅接受True 与 False的布尔型传入，例如showImg = False，默认值showImg = True
    if 'file' in kwargs or 'site' in kwargs or 'igssite' in kwargs:
        if 'file' in kwargs:
            # 获取站点文件参数，读取文件内站点信息
            siteinfo = readsiteinfo(kwargs['file'])
        elif 'site' in kwargs:
            # 获取站点信息
            siteinfo = kwargs['site']
        elif 'igssite' in kwargs:
            siteinfo = {}
            from gnssbox.lib.mgexSite import mgexSiteInfo
            for igsSiteName in kwargs['igssite']:
                if igsSiteName in mgexSiteInfo:
                    siteinfo[igsSiteName] = {'L': mgexSiteInfo[igsSiteName]['L'],
                                             'B': mgexSiteInfo[igsSiteName]['B']}
    else:
        print('未正确输入参数！')
        sys.exit()
        
    if 'autoLB' in kwargs:
        if kwargs['autoLB'] and 'L' in kwargs:
            print('不可同时传入自动确定绘图范围和手动指定范围')
            sys.exit()
    
    if 'autoLB' in kwargs:
        if kwargs['autoLB']:
            lmax = -360.0
            lmin = 360.0
            bmax = -180.0
            bmin = 180.0
            for site in siteinfo:
                if siteinfo[site]['L'] > lmax:
                    lmax =  siteinfo[site]['L']
                if  siteinfo[site]['L'] < lmin:
                    lmin =  siteinfo[site]['L']
                if  siteinfo[site]['B'] > bmax:
                    bmax =  siteinfo[site]['B']
                if  siteinfo[site]['B'] < bmin:
                    bmin =  siteinfo[site]['B']
            L_range = [lmin - 10.0, lmax + 10.0]
            B_range = [bmin - 10.0, bmax + 10.0]
            L_mid = (lmax - lmin) / 2.0
    else:
        if 'L' in kwargs:
            # 获取指定的经度范围，并通过范围获取经度中心线
            L_range = kwargs['L']
            L_mid = (kwargs['L'][1] - kwargs['L'][0]) / 2.0
        else:
            # 未指定则未-180°到180°，中心线为150°
            L_range = [-180, 180]
            L_mid = 150
        if 'B' in kwargs:
            # 同经度设置
            B_range = kwargs['B']
        else:
            B_range = [-90, 90]
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
    
    # 调用cartoplot绘制站点
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

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
    # 判断绘图范围
    if L_range == [-180, 180] and B_range == [-90, 90]:
        # 绘制全球, 经度中心线为150°
        ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=150))
        # 设置范围
        ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
        # 经度标注范围
        ax.set_xticks([0, 60, 120, 180, 240, 300, 360], crs=ccrs.PlateCarree())
        # 维度标注范围
        ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())
    else:
        ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=L_mid))
        L_tricks = []
        if L_range[1] - L_range[0] > 30:
            # 经度跨度大于30°时，经度刻度为30°
            for ll in range(int(L_range[0]), int(L_range[1]) + 1):
                if ll % 30 == 0:
                    L_tricks.append(ll)
        elif 10 < L_range[1] - L_range[0] < 30:
            # 经度跨度大于10°小于30°时，经度刻度为10°
            for ll in range(int(L_range[0]), int(L_range[1]) + 1):
                if ll % 10 == 0:
                    L_tricks.append(ll)
        else:
            # 只标注两边
            L_tricks = L_range

        B_tricks = []
        if B_range[1] - B_range[0] > 30:
            # 刻度标注同经度
            for bb in range(int(B_range[0]), int(B_range[1]) + 1):
                if bb % 30 == 0:
                    B_tricks.append(bb)
        elif 10 < B_range[1] - B_range[0] < 30:
            for bb in range(int(B_range[0]), int(B_range[1]) + 1):
                if bb % 10 == 0:
                    B_tricks.append(bb)
        else:
            B_tricks = B_range
        # 经纬度范围与刻度
        ax.set_extent([L_range[0], L_range[1], B_range[0], B_range[1]], crs=ccrs.PlateCarree())
        ax.set_xticks(L_tricks, crs=ccrs.PlateCarree())
        ax.set_yticks(B_tricks, crs=ccrs.PlateCarree())
    
    if addFeat:
        # 添加陆地
        ax.add_feature(cfeature.LAND)
        # 添加海洋
        ax.add_feature(cfeature.OCEAN)
        # 添加海岸线
        ax.add_feature(cfeature.COASTLINE, linewidth=0.1)

    for site in siteinfo:
        # 判断站点是否在指定范围内，未在范围内则不进行绘制
        if L_range[1] > siteinfo[site]['L'] > L_range[0] and B_range[1] > siteinfo[site]['B'] > B_range[0]:
            # 绘制站点，三角形\红色\大小7.0
            ax.plot(siteinfo[site]['L'], siteinfo[site]['B'], '^', color='r', mec='k', mew=0, transform=ccrs.Geodetic(),
                    ms=7.0)
            # 添加站名标注，站名向西3°，向北2°,字体大小10
            plt.text(siteinfo[site]['L'] - 3, siteinfo[site]['B'] + 3, site, transform=ccrs.Geodetic(),
                     fontsize=10)
            # xy轴标注大小为x-large
    plt.xticks(fontsize='x-large')
    plt.yticks(fontsize='x-large')
    # 经纬线格式设置
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    # 是否保存文件
    if savePng:
        fig.savefig(savePngPath, bbox_inches='tight', dpi=400)
    # 是否展示图
    if showImg:
        plt.show()
