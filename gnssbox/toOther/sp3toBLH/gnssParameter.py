# 1. 坐标系统
# 1.1 椭球参数类
class coordSystemPara:
    def __init__(self, a, f, GM, omega):
        import math
        self.a = a
        self.f = f
        self.GM = GM
        self.omega = omega
        self.e2 = f * (2.0 - f)
        self.e = math.sqrt(self.e2)
        self.b = a * math.sqrt(1.0 - self.e2)
        self.eprime = math.sqrt(a ** 2 - self.b ** 2) / self.b


# 1.1 椭球参数, 对应class coordSystemPara
coordSystem = {'WGS84': coordSystemPara(6378137.0, 1.0 / 298.257223563, 3.986004415e14, 7.2921151467e-5),
               'CGCS2000': coordSystemPara(6378137.0, 1.0 / 298.257222101, 3.986004418e14, 7.292115e-5),
               'BDS': coordSystemPara(6378137.0, 1.0 / 298.257222101, 3.986004418e14, 7.292115e-5),
               'PZ90': coordSystemPara(6378136.0, 1.0 / 298.257840000, 3.986004418e14, 7.2921151467e-5),
               'GTRF': coordSystemPara(6378136.5, 1.0 / 298.257690000, 3.986004415e14, 7.292115e-5),
               'GRS80':coordSystemPara(6378137, 1.0 / 298.257222100882711243, 3.986005e14, 7.292115e-5)}

# 2. 卫星导航系统信息
# 2.1 卫星系统
satelliteSyetem = {'BDS', 'GLO', 'GPS', 'GAL', 'IRNSS', 'QZSS'}
# 2.2 北斗轨道类型
BDSoribt = {"C01": "GEO", "C02": "GEO", "C03": "GEO", "C04": "GEO", "C05": "GEO", "C06": "IGSO", "C07": "IGSO",
            "C08": "IGSO", "C09": "IGSO", "C10": "IGSO", "C11": "MEO", "C12": "MEO", "C13": "IGSO", "C14": "MEO",
            "C16": "IGSO", "C18": "IGSO", "C19": "MEO", "C20": "MEO", "C21": "MEO", "C22": "MEO", "C23": "MEO",
            "C24": "MEO", "C25": "MEO", "C26": "MEO", "C27": "MEO", "C28": "MEO", "C29": "MEO", "C30": "MEO",
            "C31": "IGSO", "C32": "MEO", "C33": "MEO", "C34": "MEO", "C35": "MEO", "C36": "MEO", "C37": "MEO",
            "C38": "IGSO", "C39": "IGSO", "C40": "IGSO", "C41": "MEO", "C42": "MEO", "C43": "MEO", "C44": "MEO",
            "C45": "MEO", "C46": "MEO", "C57": "MEO", "C58": "MEO", "C59": "GEO", "C60": "GEO", "C61": "GEO"}
