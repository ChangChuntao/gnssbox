import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

from gnssbox.ioGnss import readsp3

def plotSatTrack(**kwargs):
    print(kwargs)
    if 'sp3file' in kwargs:
        print('sss')