import datetime
from gnssbox.lib.gnssTime import gnssTimesTran

outtime = gnssTimesTran(From = 'GPSWEEKD', To = 'GPSWEEKD', Time = [2222, 0])
print(outtime)