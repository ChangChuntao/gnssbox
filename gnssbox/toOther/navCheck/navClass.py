class gpsNav(object):
    def __init__(self, Epoch = None, SVclockBias = None, SVclockDrift = None, SVclockDriftRate = None,
                IODE = None, Crs = None, DeltaN = None, M0 = None, 
                Cuc = None, e = None, Cus = None, sqrtA = None,
                toe = None, Cic = None, OMEGA0 = None, Cis = None,
                i0 = None, Crc = None, omega = None, OMEGA_DOT = None,
                IDOT = None, L2Codes = None, GPS_Week = None, L2PdataFlag = None,
                SVaccuracy = None, SVhealth = None, TGD = None, IODC = None,
                Transmission = None, FitIntervalHours = None):
        self.Epoch = Epoch
        self.SVclockBias = SVclockBias
        self.SVclockDrift = SVclockDrift
        self.SVclockDriftRate = SVclockDriftRate
        self.IODE = IODE
        self.Crs = Crs
        self.DeltaN = DeltaN
        self.M0 = M0
        self.Cuc = Cuc
        self.e = e
        self.Cus = Cus
        self.sqrtA = sqrtA
        self.toe = toe
        self.Cic = Cic
        self.OMEGA0 = OMEGA0
        self.Cis = Cis
        self.i0 = i0
        self.Crc = Crc
        self.omega = omega
        self.OMEGA_DOT = OMEGA_DOT
        self.IDOT = IDOT
        self.L2Codes = L2Codes
        self.GPS_Week = GPS_Week
        self.L2PdataFlag = L2PdataFlag
        self.SVaccuracy = SVaccuracy
        self.SVhealth = SVhealth
        self.TGD = TGD
        self.IODC = IODC
        self.Transmission = Transmission
        self.FitIntervalHours = FitIntervalHours
        

class galileoNav(object):
    def __init__(self, Epoch = None, SVclockBias = None, SVclockDrift = None, SVclockDriftRate = None,
                IODnav = None, Crs = None, DeltaN = None, M0 = None, 
                Cuc = None, e = None, Cus = None, sqrtA = None,
                toe = None, Cic = None, OMEGA0 = None, Cis = None,
                i0 = None, Crc = None, omega = None, OMEGA_DOT = None,
                IDOT = None, DataSources = None, GAL_Week = None, Spare = None,
                SISA = None, SVhealth = None, BGD_E5a_E1 = None, BGD_E5b_E1 = None,
                Transmission = None):
        self.Epoch = Epoch
        self.SVclockBias = SVclockBias
        self.SVclockDrift = SVclockDrift
        self.SVclockDriftRate = SVclockDriftRate
        self.IODnav = IODnav
        self.Crs = Crs
        self.DeltaN = DeltaN
        self.M0 = M0
        self.Cuc = Cuc
        self.e = e
        self.Cus = Cus
        self.sqrtA = sqrtA
        self.toe = toe
        self.Cic = Cic
        self.OMEGA0 = OMEGA0
        self.Cis = Cis
        self.i0 = i0
        self.Crc = Crc
        self.omega = omega
        self.OMEGA_DOT = OMEGA_DOT
        self.IDOT = IDOT
        self.DataSources = DataSources
        self.GAL_Week = GAL_Week
        self.Spare = Spare
        self.SISA = SISA
        self.SVhealth = SVhealth
        self.BGD_E5a_E1 = BGD_E5a_E1
        self.BGD_E5b_E1 = BGD_E5b_E1
        self.Transmission = Transmission
        
        
class glonassNav(object):
    def __init__(self, Epoch = None, SVclockBias = None, SVrelativeFrequencyBias  = None, MessageFrameTime = None,
                posX = None, velX = None, accelerationX = None, health = None, 
                posY = None, velY = None, accelerationY = None, frequency = None,
                posZ = None, velZ = None, accelerationZ = None, operAge = None,
                StatusFlags = None, delayDif = None, URAI = None, HealthFlags = None):
        self.Epoch = Epoch
        self.SVclockBias = SVclockBias
        self.SVrelativeFrequencyBias = SVrelativeFrequencyBias
        self.MessageFrameTime = MessageFrameTime
        self.posX = posX
        self.velX = velX
        self.accelerationX = accelerationX
        self.health = health
        self.posY = posY
        self.velY = velY
        self.accelerationY = accelerationY
        self.frequency = frequency
        self.posZ = posZ
        self.velZ = velZ
        self.accelerationZ = accelerationZ
        self.operAge = operAge
        self.StatusFlags = StatusFlags
        self.delayDif = delayDif
        self.URAI = URAI
        self.HealthFlags = HealthFlags
        
        
class bdsNav(object):
    def __init__(self, Epoch = None, SVclockBias = None, SVclockDrift = None, SVclockDriftRate = None,
                AODE = None, Crs = None, DeltaN = None, M0 = None, 
                Cuc = None, e = None, Cus = None, sqrtA = None,
                toe = None, Cic = None, OMEGA0 = None, Cis = None,
                i0 = None, Crc = None, omega = None, OMEGA_DOT = None,
                IDOT = None, Spare1 = None, BDT_Week = None, Spare2 = None,
                SVaccuracy = None, SatH1 = None, TGD1 = None, TGD2 = None,
                Transmission = None, AODC = None):
        self.Epoch = Epoch
        self.SVclockBias = SVclockBias
        self.SVclockDrift = SVclockDrift
        self.SVclockDriftRate = SVclockDriftRate
        self.AODE = AODE
        self.Crs = Crs
        self.DeltaN = DeltaN
        self.M0 = M0
        self.Cuc = Cuc
        self.e = e
        self.Cus = Cus
        self.sqrtA = sqrtA
        self.toe = toe
        self.Cic = Cic
        self.OMEGA0 = OMEGA0
        self.Cis = Cis
        self.i0 = i0
        self.Crc = Crc
        self.omega = omega
        self.OMEGA_DOT = OMEGA_DOT
        self.IDOT = IDOT
        self.Spare1 = Spare1
        self.BDT_Week = BDT_Week
        self.Spare2 = Spare2
        self.SVaccuracy = SVaccuracy
        self.SatH1 = SatH1
        self.TGD1 = TGD1
        self.TGD2 = TGD2
        self.Transmission = Transmission
        self.AODC = AODC
        
class qzssNav(object):
    def __init__(self, Epoch = None, SVclockBias = None, SVclockDrift = None, SVclockDriftRate = None,
                IODE = None, Crs = None, DeltaN = None, M0 = None, 
                Cuc = None, e = None, Cus = None, sqrtA = None,
                toe = None, Cic = None, OMEGA0 = None, Cis = None,
                i0 = None, Crc = None, omega = None, OMEGA_DOT = None,
                IDOT = None, L2Codes = None, GPS_Week = None, L2PdataFlag = None,
                SVaccuracy = None, SVhealth = None, TGD = None, IODC = None,
                Transmission = None, FitIntervalFlag = None):
        self.Epoch = Epoch
        self.SVclockBias = SVclockBias
        self.SVclockDrift = SVclockDrift
        self.SVclockDriftRate = SVclockDriftRate
        self.IODE = IODE
        self.Crs = Crs
        self.DeltaN = DeltaN
        self.M0 = M0
        self.Cuc = Cuc
        self.e = e
        self.Cus = Cus
        self.sqrtA = sqrtA
        self.toe = toe
        self.Cic = Cic
        self.OMEGA0 = OMEGA0
        self.Cis = Cis
        self.i0 = i0
        self.Crc = Crc
        self.omega = omega
        self.OMEGA_DOT = OMEGA_DOT
        self.IDOT = IDOT
        self.L2Codes = L2Codes
        self.GPS_Week = GPS_Week
        self.L2PdataFlag = L2PdataFlag
        self.SVaccuracy = SVaccuracy
        self.SVhealth = SVhealth
        self.TGD = TGD
        self.IODC = IODC
        self.Transmission = Transmission
        self.FitIntervalFlag = FitIntervalFlag
        
        
class sbasNav(object):
    def __init__(self, Epoch = None, SVclockBias = None, SVrelativeFrequencyBias  = None, Transmission = None,
                posX = None, velX = None, accelerationX = None, health = None, 
                posY = None, velY = None, accelerationY = None, AccuracyCode = None,
                posZ = None, velZ = None, accelerationZ = None, IODN = None):
        self.Epoch = Epoch
        self.SVclockBias = SVclockBias
        self.SVrelativeFrequencyBias = SVrelativeFrequencyBias
        self.Transmission = Transmission
        self.posX = posX
        self.velX = velX
        self.accelerationX = accelerationX
        self.health = health
        self.posY = posY
        self.velY = velY
        self.accelerationY = accelerationY
        self.AccuracyCode = AccuracyCode
        self.posZ = posZ
        self.velZ = velZ
        self.accelerationZ = accelerationZ
        self.IODN = IODN
        
class irnssNav(object):
    def __init__(self, Epoch = None, SVclockBias = None, SVclockDrift = None, SVclockDriftRate = None,
                IODEC = None, Crs = None, DeltaN = None, M0 = None, 
                Cuc = None, e = None, Cus = None, sqrtA = None,
                toe = None, Cic = None, OMEGA0 = None, Cis = None,
                i0 = None, Crc = None, omega = None, OMEGA_DOT = None,
                IDOT = None, Blank = None, IRN_Week = None, Spare1 = None,
                RangeAccuracy = None, Health = None, TGD = None, Spare2 = None,
                Transmission = None):
        self.Epoch = Epoch
        self.SVclockBias = SVclockBias
        self.SVclockDrift = SVclockDrift
        self.SVclockDriftRate = SVclockDriftRate
        self.IODEC = IODEC
        self.Crs = Crs
        self.DeltaN = DeltaN
        self.M0 = M0
        self.Cuc = Cuc
        self.e = e
        self.Cus = Cus
        self.sqrtA = sqrtA
        self.toe = toe
        self.Cic = Cic
        self.OMEGA0 = OMEGA0
        self.Cis = Cis
        self.i0 = i0
        self.Crc = Crc
        self.omega = omega
        self.OMEGA_DOT = OMEGA_DOT
        self.IDOT = IDOT
        self.Blank = Blank
        self.IRN_Week = IRN_Week
        self.Spare1 = Spare1
        self.RangeAccuracy = RangeAccuracy
        self.Health = Health
        self.TGD = TGD
        self.Spare2 = Spare2
        self.Transmission = Transmission