# # # 通过站点文件绘制地图
from gnssbox.plot.plotSite import plotSite

plotSite(file=r"gnssbox\plot\example\site.info", autoLB=True,)
# # 通过站点信息绘制站点图
# site = {'JOZE': {'L': 21.03139, 'B': 52.09722},
#         'TIXI': {'L': 128.86639, 'B': 71.63444},
#         'IISC': {'L': 77.57028, 'B': 13.02111}}
# plotSite.plotSite(site=site)
# # 指定绘制范围
site = {'JOZE': {'L': 21.03139, 'B': 52.09722},
        'TIXI': {'L': 128.86639, 'B': 71.63444},
        'IISC': {'L': 77.57028, 'B': 13.02111}}
plotSite(site=site, L=[0, 270], B=[-60, 60])
# # 指定mgex站点
from gnssbox.plot.plotSite import plotSite

site = ['bjfs', 'irkj', 'urum', 'abpo', 'joze', 'tixi']
plotSite(igssite=site, autoLB=True, addFeat=False)

# # 绘制卫星天空图
from datetime import datetime
from gnssbox.plot.plotSatSky import plotSatSky

plotSatSky(sp3File=r'gnssbox\ioGnss\Example\wum21921.sp3',
           coord=[1337936.455, 6070317.1261, 1427876.7852],
           datetime=datetime(2022, 1, 10, 0, 15, 0))

# # 绘制卫星轨迹
from gnssbox.plot.plotSatTrack import plotSatTrack

# plotSatTrack(r'D:\Code\CodeTest\whu20696.sp3')
plotSatTrack(r'gnssbox\ioGnss\Example\wum21921.sp3', system=['C', 'G'])
