

def sat2siteAngle(satX, satY, satZ, siteX, siteY, siteZ):
    import math
    from gnssbox.coordTran.xyz2neu import xyz2neu
    from gnssbox.coordTran.xyz2blh import xyz2blh
    from gnssbox.coordTran.xy2azi import xy2azi    
    System = 'WGS84'
    north, east, up = xyz2neu(siteX, siteY, siteZ, satX, satY, satZ, System)
    siteB, siteL, H = xyz2blh(siteX, siteY, siteZ, System)
    satB, satL, H = xyz2blh(satX, satY, satZ, System)
    Azi = xy2azi(siteL, siteB, satL, satB)
    Ele = math.atan(up / math.sqrt(north * north + east * east))
    Zenith = math.pi/2 - Ele
    return Zenith, Azi, Ele