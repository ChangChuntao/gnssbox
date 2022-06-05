# 2022.06.03 : 读取站点信息文件，并返回为sp3Data
#              by ChangChuntao -> Version : 1.00
def readsiteinfo(sitefile):
    # 简易站点信息文件，文件格式：
    # | L1 B1 SITE_NAME1 |
    # | L2 B2 SITE_NAME2 |
    # | ................ |
    # | LN BN SITE_NAMEN |
    sitefile_line = open(sitefile, 'r+').readlines()
    siteinfo = {}
    for line in sitefile_line:
        if len(line) > 1:
            siteinfo[line.split()[2]] = {'L': float(line.split()[0]), 'B': float(line.split()[1])}
    return siteinfo