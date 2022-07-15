import sys
from navSatCheck import navSatCheck
args = sys.argv
if len(args) == 4 or len(args) == 3:
    navFile = args[1]
    rinexFile = args[2]
    outFile = None
    if len(args) == 4:
        outFile = args[3]
else:
    print('')
    print('Usage: ' + args[0].split('\\')[-1] + ' <navFile> <rinexFile> <outFile(optional)>')
    sys.exit()

# navFile = r'D:\Code\gnssbox\gnssbox\toOther\navCheck\testDir\GAMG00KOR_R_20220010000_01D_MN.rnx'
# rinexFile = r'D:\Code\gnssbox\gnssbox\toOther\navCheck\testDir\GAMG00KOR_R_20220010000_01D_30S_MO.rnx'
# outFile = r'D:\Code\gnssbox\gnssbox\toOther\navCheck\testDir\GAMP_NAV_RINEX.txt'

navSatCheck(navFile, rinexFile, outFile)