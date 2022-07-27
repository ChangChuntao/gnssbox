# # # # 通过站点文件绘制地图
from gnssbox.plot.plotSite import plotSite

# plotSite(file=r"gnssbox\plot\example\site.info", autoLB=True,)
# # # 通过站点信息绘制站点图
# # site = {'JOZE': {'L': 21.03139, 'B': 52.09722},
# #         'TIXI': {'L': 128.86639, 'B': 71.63444},
# #         'IISC': {'L': 77.57028, 'B': 13.02111}}
# plotSite.plotSite(site=site)
# # 指定绘制范围
# site = {'QQDX': {'L': 123.72878186937216, 'B': 46.8890057409281},
#         'QQJH': {'L': 123.92401028973711, 'B': 47.37656311895193},
#         'QQLJ': {'L': 123.24534846024723, 'B': 47.30006995317775},
#         'CHAN': {'L': 125.4442042087, 'B': 43.7906851005},
#         'SHAO': {'L': 121.2004490631, 'B': 31.0996409372},
#         'BJFS': {'L': 115.8924903180, 'B': 39.6085999910},
#         'JFNG': {'L': 114.4910212787, 'B': 30.5155647484},}
# plotSite(site=site, autoLB=True)
# # # 指定mgex站点
# from gnssbox.plot.plotSite import plotSite

# site = ['aira', 'badg', 'bjfs', 'bjnm', 'chan', 'chof', 'dae2', 'daej', 'gamg', 'irkj', 'irkm', 'jfng', 'kgni', 'mssa', 'mtka', 'osn3', 'osn4', 'sejn', 'shao', 'smst', 'suwn', 'ulab', 'usud', 'wuh2', 'wuhn', 'yakt', 'yons']
# site = ['bjfs', 'chan', 'jfng', 'osn3', 'shao', 'whu2']
# plotSite(igssite=site, autoLB=True)

# # # 绘制卫星天空图
# from datetime import datetime
# from gnssbox.plot.plotSatSky import plotSatSky

# plotSatSky(sp3File=r'gnssbox\ioGnss\Example\wum21921.sp3',
#            coord=[1337936.455, 6070317.1261, 1427876.7852],
#            datetime=datetime(2022, 1, 10, 0, 15, 0))

# # 绘制卫星轨迹
from gnssbox.plot.plotSatTrack import plotSatTrack

plotSatTrack(r'D:\Project\NOW\NSOAS\NSOAS\PODDATA\GF3B\PRJ\ROE\2022\2022205193120\gf3b22141.sp3')
# plotSatTrack(r'D:\Project\NOW\WB\1503\decode\00\00.sp3')