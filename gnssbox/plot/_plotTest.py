# 通过站点文件绘制地图
# from gnssbox.plot import plotSite
# plotSite.plotSite(file=r"D:\Code\gnssbox\gnssbox\plot\example\site.info")
# # 通过站点信息绘制站点图
# site = {'JOZE': {'L': 21.03139, 'B': 52.09722},
#         'TIXI': {'L': 128.86639, 'B': 71.63444},
#         'IISC': {'L': 77.57028, 'B': 13.02111}}
# plotSite.plotSite(site=site)
# # 指定绘制范围
# site = {'JOZE': {'L': 21.03139, 'B': 52.09722},
#         'TIXI': {'L': 128.86639, 'B': 71.63444},
#         'IISC': {'L': 77.57028, 'B': 13.02111}}
# plotSite.plotSite(site=site, L=[0, 270], B=[-60, 60])

# 绘制卫星天空图
from datetime import datetime
from gnssbox.plot import plotSatSky

plotSatSky.plotSatSky(sp3File=r'D:\Code\gnssbox\gnssbox\ioGnss\Example\wum21921.sp3',
                      coord=[1916269.343, 6029977.689, -801719.821],
                      datetime=datetime(2022, 1, 10, 0, 15, 0))
