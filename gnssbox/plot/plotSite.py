
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

from ioGnss.readsiteinfo import readsiteinfo


def cartoplot(siteinfo, L_range, B_range, L_mid):
    mpl.rcParams['axes.unicode_minus'] = False
    mpl.rc('xtick', labelsize=9)
    mpl.rc('ytick', labelsize=9)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'

    fig = plt.figure(figsize=(14, 7))
    if L_range == [-180, 180] and B_range == [-90, 90]:
        ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=150))
        ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
        ax.set_xticks([0, 60, 120, 180, 240, 300, 360], crs=ccrs.PlateCarree())
        ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())
    else:

        ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=L_mid))
        L_tricks = []
        if L_range[1] - L_range[0] > 30:
            for ll in range(int(L_range[0]), int(L_range[1]) + 1):
                if ll % 30 == 0:
                    L_tricks.append(ll)
        elif 10 < L_range[1] - L_range[0] < 30:
            for ll in range(int(L_range[0]), int(L_range[1]) + 1):
                if ll % 10 == 0:
                    L_tricks.append(ll)
        else:
            L_tricks = L_range

        B_tricks = []
        if B_range[1] - B_range[0] > 30:
            for bb in range(int(B_range[0]), int(B_range[1]) + 1):
                if bb % 30 == 0:
                    B_tricks.append(bb)
        elif 10 < B_range[1] - B_range[0] < 30:
            for bb in range(int(B_range[0]), int(B_range[1]) + 1):
                if bb % 10 == 0:
                    B_tricks.append(bb)
        else:
            B_tricks = B_range
        print(L_tricks)
        ax.set_extent([L_range[0], L_range[1], B_range[0], B_range[1]], crs=ccrs.PlateCarree())
        ax.set_xticks(L_tricks, crs=ccrs.PlateCarree())
        ax.set_yticks(B_tricks, crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE, linewidth=0.1)

    for site in siteinfo:
        if L_range[1] > siteinfo[site]['L'] > L_range[0] and B_range[1] > siteinfo[site]['B'] > B_range[0]:
            ax.plot(siteinfo[site]['L'], siteinfo[site]['B'], '^', color='r', mec='k', mew=0, transform=ccrs.Geodetic(),
                    ms=7.0)
            plt.text(siteinfo[site]['L'] - 6, siteinfo[site]['B'] + 3, site, transform=ccrs.Geodetic(),
                     fontsize=10)  # 添加站名标注，站名向西6°，向北3°
    plt.xticks(fontsize='x-large')
    plt.yticks(fontsize='x-large')
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)

    # fig.savefig('global_sitemap.png', bbox_inches='tight', dpi=400)
    plt.show()


def plotSite(**kwargs):
    print(kwargs)
    if 'file' in kwargs:
        siteinfo = readsiteinfo(kwargs['file'])
    else:
        if 'site' in kwargs:
            siteinfo = kwargs['site']
        else:
            print('未正确输入参数！')
            return 0
    if 'L' in kwargs:
        L_range = kwargs['L']
        L_mid = (kwargs['L'][1] - kwargs['L'][0]) / 2.0
    else:
        L_range = [-180, 180]
        L_mid = 150
    if 'B' in kwargs:
        B_range = kwargs['B']
    else:
        B_range = [-90, 90]
    cartoplot(siteinfo, L_range, B_range, L_mid)
