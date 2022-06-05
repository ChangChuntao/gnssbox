import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from readsp3 import readSp3Head, readSp3

sp3File = r'D:\Code\gnssbox\gnssbox\ioGnss\Example\wum21921.sp3'
sp3Data = readSp3(sp3File)
prn = 'C01'
print(sp3Data[prn][2].epoch)
for epochData in sp3Data[prn]:
    print(epochData.epoch, epochData.clk)