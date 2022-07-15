navFile = r'D:\Code\gnssbox\gnssbox\dataAnalysis\test\GAMG00KOR_R_20220010000_01D_MN.rnx'
# rinexFile = r'D:\Code\gnssbox\gnssbox\dataAnalysis\test\GAMG00KOR_R_20220010000_01D_30S_MO.rnx'
# outFile = r'D:\Code\gnssbox\gnssbox\dataAnalysis\test\GAMP_NAV_RINEX.txt'
# from gnssbox.dataAnalysis.navSatCheck import navSatCheck
# # a = datetime.datetime(2022, 1, 1, 17, 16, 30)
# # b = datetime.datetime(2022, 1, 1, 18)
# # print((b-a).days)
# navSatCheck(navFile, rinexFile, outFile)


navBrdmFile = r'D:\Code\gnssbox\gnssbox\dataAnalysis\test\BRDM00DLR_S_20220010000_01D_MN.rnx'
from gnssbox.dataAnalysis.navDif import navDif

navDif(navFile, navBrdmFile)
