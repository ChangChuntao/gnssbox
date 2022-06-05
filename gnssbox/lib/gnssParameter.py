class coordSystemPara:
    def __init__(self, a, f, GM, omega):
        self.a = a
        self.f = f
        self.GM = GM
        self.omega = omega

coordSystem = {}
coordSystem['WGS84'] = coordSystemPara(6378137.0, 1.0/298.257223563, 3.986004415e14, 7.2921151467e-5)
coordSystem['CGCS2000'] = coordSystemPara(6378137.0, 1.0/298.257222101, 3.986004418e14, 7.292115e-5)
coordSystem['BDS'] = coordSystemPara(6378137.0, 1.0/298.257222101, 3.986004418e14, 7.292115e-5)