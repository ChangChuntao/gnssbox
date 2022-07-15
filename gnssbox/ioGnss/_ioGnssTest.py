# readsp3 测试
# from gnssbox.ioGnss.readSp3 import readSp3Head
# from gnssbox.ioGnss.delSp3Sat import delSp3Sat
# sp3File = r'D:\Code\gnssbox\gnssbox\ioGnss\Example\hour22022_00.sp3'
# # sp3Data = readSp3Head(sp3File)
# outputFile = r'D:\Code\gnssbox\gnssbox\ioGnss\Example\del.txt'
# delSp3Sat(sp3File, ['R', 'E', 'J', 'I'], outputFile)

# prn = 'C01'
# for epochData in sp3Data[prn]:
#     print(epochData.epoch, epochData.clk)

# readPandaAtt 测试
# from gnssbox.ioGnss.interpolation import interpolationPandaAtt
# from gnssbox.ioGnss.readPandaAtt import readPandaAtt
# attFile = r'D:\Code\CodeTest\att_2022097_gf3c'
# attData = readPandaAtt(attFile)

# 内插PandaAtt 测试
# interpolationPandaAtt(attFile, 1, 'test.txt')

# sp3toClk 测试
# from gnssbox.ioGnss.sp3toClk import sp3toClk
# sp3toClk('gnssbox\ioGnss\Example\igu22122_00.sp3', 'gnssbox\ioGnss\Example\igu22122_00_clk.clk')
# import datetime
# a = [{'time': datetime.datetime(2020, 5, 19, 0, 0), 'sat': ['R01', 'R02', 'R08', 'R10', 'R11', 'R12', 'R20', 'R21', 'R22']},
#      {'time': datetime.datetime(2020, 5, 19, 0, 0), 'sat': ['R01', 'R02', 'R08', 'R10', 'R11', 'R12', 'R20', 'R21', 'R22']}]
# print(a[0])


# from gnssbox.ioGnss.readEle import readEle
#
# readEle(r'D:\Code\gnssbox\gnssbox\toOther\elesn2all\bjfs1400.ele')

# from gnssbox.ioGnss.readSn import readSn
# readSn(r'D:\Code\gnssbox\gnssbox\toOther\elesn2all\bjfs1400.sn2')

# from gnssbox.ioGnss.readclk import readClkHead

# readClkHead(r'D:\Code\gnssbox\gnssbox\ioGnss\Example\hour22022_00.clk')


# from gnssbox.ioGnss.delClkSat import delClkSat
# import datetime
# delTime = datetime.datetime(2022, 3, 22)
# outputFile = r'D:\Code\gnssbox\gnssbox\ioGnss\Example\delclk.txt'
# delClkSat(r'D:\Code\gnssbox\gnssbox\ioGnss\Example\hour22022_00.clk',   ['R', 'E', 'J', 'I'], delTime, outputFile)

# rinexFile = r'D:\Code\gnssbox\gnssbox\dataAnalysis\test\GAMG00KOR_R_20220010000_01D_30S_MO.rnx'
# from gnssbox.ioGnss.readrinex import readRinexSat
# readRinexSat(rinexFile)

from gnssbox.ioGnss.readNav import readNav


readNav(r'D:\Code\gnssbox\gnssbox\dataAnalysis\test\brdm0010.22p')