# readsp3 测试
from gnssbox.ioGnss.readSp3 import readSp3

sp3File = r'D:\Code\gnssbox\gnssbox\ioGnss\Example\wum21921.sp3'
sp3Data = readSp3(sp3File)
prn = 'C01'
for epochData in sp3Data[prn]:
    print(epochData.epoch, epochData.clk)

# readPandaAtt 测试
# from gnssbox.ioGnss.interpolation import interpolationPandaAtt
# from gnssbox.ioGnss.readPandaAtt import readPandaAtt
# attFile = r'D:\Code\CodeTest\att_2022097_gf3c'
# attData = readPandaAtt(attFile)

# 内插PandaAtt 测试
# interpolationPandaAtt(attFile, 1, 'test.txt')
