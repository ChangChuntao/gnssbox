import sys
from navDif import navDif
args = sys.argv
if len(args) == 4 or len(args) == 3:
    oriNavFile = args[1]
    comparaNavFile = args[2]
    difNavFile = None
    if len(args) == 4:
        difNavFile = args[3]
else:
    print('')
    print('Usage: ' + args[0].split('\\')[-1] + ' <oriNavFile> <comparaNavFile> <difNavFile(optional)>')
    sys.exit()

# python .\_mainNavDif.py D:\Code\gnssbox\gnssbox\toOther\navCheck\testDir\GAMG00KOR_R_20220010000_01D_MN.rnx D:\Code\gnssbox\gnssbox\toOther\navCheck\testDir\BRDM00DLR_S_20220010000_01D_MN.rnx

# 根据情况修改量级！！！！！
OrderOfMagnitude = 1e-13

navDif(oriNavFile, comparaNavFile, OrderOfMagnitude, difNavFile)