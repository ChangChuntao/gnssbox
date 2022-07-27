import os
from gnssbox.getGnssData.getHour import getHour
from gnssbox.lib.gnssTime import doy2gpswd
FAST = 'D:\Code\gnssbox\gnssbox\getGnssData\FAST\Windows\FAST.exe'

getHour(FAST, 2022, 161, 171, r'D:\Project\NOW\NSOAS\03-CodeTest\workdir\gf3_gps_roe_whu_pro\G3B\whu\gnss\products')
# import gnssbox.lib.filePy
# fileList = gnssbox.lib.filePy.getFileInPath('D:\Code\CodeTest')
# for SP3 in fileList:
#     if 'WUM0MGXULA' in SP3 and str(SP3).split('.')[-1] == 'SP3':
#             year = int(str(SP3).split('WUM0MGXULA_')[-1][0:4])
#             doy = int(str(SP3).split('WUM0MGXULA_')[-1][4:7])
#             hour = int(str(SP3).split('WUM0MGXULA_')[-1][7:9])
#             [gpsweek, gpsweekD] = doy2gpswd(year, doy)
#             hourFile = 'hour' + str(gpsweek) + str(gpsweekD) + '_' + '%02d' % hour +  ".sp3"
#             hourFile = os.sep.join(['D:\Code\CodeTest', hourFile])
#             os.rename(SP3, hourFile)