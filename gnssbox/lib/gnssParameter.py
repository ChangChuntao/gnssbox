# 1. 坐标系统
class coordSystemPara:
    def __init__(self, a, f, GM, omega):
        self.a = a
        self.f = f
        self.GM = GM
        self.omega = omega


# 1.1 椭球参数, 对应class coordSystemPara
coordSystem = {'WGS84': coordSystemPara(6378137.0, 1.0 / 298.257223563, 3.986004415e14, 7.2921151467e-5),
               'CGCS2000': coordSystemPara(6378137.0, 1.0 / 298.257222101, 3.986004418e14, 7.292115e-5),
               'BDS': coordSystemPara(6378137.0, 1.0 / 298.257222101, 3.986004418e14, 7.292115e-5)}

# 2. 卫星导航系统信息
satelliteSyetem = ['BDS', 'GLO', 'GPS', 'GAL', 'SBAS', 'IRNSS', 'QZSS', 'LEO']
