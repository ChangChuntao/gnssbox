def readsiteinfo(sitefile):
    sitefile_line = open(sitefile, 'r+').readlines()
    siteinfo = {}
    for line in sitefile_line:
        if len(line) > 1:
            siteinfo[line.split()[2]] = {'L': float(line.split()[0]), 'B': float(line.split()[1])}
    return siteinfo
