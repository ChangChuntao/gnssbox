# import datetime
# from gnssbox.lib.gnssTime import gnssTimesTran

# outtime = gnssTimesTran(From = 'YDOY', To = 'YMD', Time = [2020, 1])
# print(outtime)
# outtime = gnssTimesTran(From = 'YDOY', To = 'MJDSOD', Time = [2020, 1])
# print(outtime)

# from gnssTime import *
# print(gpswd2ymd(2200,1))

from gnssbox.lib.batchRename import batchRename

path = r'D:\Project\NOW\NSOAS\03-CodeTest\workdir\gf3_gps_l0a\G3B\PODS\RE_PROCESS\ATT'
batchRename(path, 'ATT_', 'G3B_OPER_ATT_OBSL1A_')