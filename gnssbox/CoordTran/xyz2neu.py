

def xyz2neu(originX, originY, originZ, X, Y, Z, System):
    import math
    from gnssbox.coordTran.xyz2blh import xyz2blh
    deltaX = X - originX
    deltaY = Y - originY
    deltaZ = Z - originZ
    [lat, lon, h] = xyz2blh(originX, originY, originZ, System)
    north = (-math.sin(lat) * math.cos(lon) * deltaX -
             math.sin(lat) * math.sin(lon) * deltaY +
             math.cos(lat) * deltaZ)
    east = -math.sin(lon) * deltaX + math.cos(lon) * deltaY
    up = (math.cos(lat) * math.cos(lon) * deltaX +
          math.cos(lat) * math.sin(lon) * deltaY +
          math.sin(lat) * deltaZ)
    return north, east, up