import shutil


def getHour(FAST, year, doy1, doy2, outputPath = None):
    import os
    import time
    from gnssbox.lib.gnssTime import doy2gpswd
    from gnssbox.lib.filePy import getFileInPath
    from gnssbox.lib.filePy import mkdir
    print(year, doy1, doy2, outputPath)
    for doy in range(doy1, doy2 + 1):
        [nowWeek,nowDow] = doy2gpswd(year, doy)
        wdPath = os.sep.join([outputPath, str(nowWeek)])
        mkdir(wdPath)
    #     fastArg = FAST + ' -t MGEX_WUHU_sp3 '
    #     fastArg += '-y ' + str(year) + ' ' 
    #     fastArg += '-d ' + str(doy) + ' ' 
    #     fastArg += '-l ' + wdPath + ' '
    #     fastArg += '-p 8'
    #     os.system(fastArg)
    #     time.sleep(1)
    #     fileList = getFileInPath(wdPath)
    #     for SP3 in fileList:
    #         if 'WUM0MGXULA' in SP3 and str(SP3).split('.')[-1] == 'SP3':
    #             year = int(str(SP3).split('WUM0MGXULA_')[-1][0:4])
    #             doy = int(str(SP3).split('WUM0MGXULA_')[-1][4:7])
    #             hour = int(str(SP3).split('WUM0MGXULA_')[-1][7:9])
    #             [gpsweek, gpsweekD] = doy2gpswd(year, doy)
    #             hourFile = 'hour' + str(gpsweek) + str(gpsweekD) + '_' + '%02d' % (hour) +  ".sp3"
    #             hourFile = os.sep.join([wdPath, hourFile])
    #             os.rename(SP3, hourFile)
        
        fastArg = FAST + ' -t GPS_IGS_clk '
        fastArg += '-y ' + str(year) + ' ' 
        fastArg += '-d ' + str(doy) + ' '  
        fastArg += '-l ' + wdPath + ' '
        fastArg += '-p 8'
        os.system(fastArg)
        time.sleep(1)
        fileList = getFileInPath(wdPath)
        for CLK in fileList:
            # if 'WUM0MGXULA' in CLK and str(CLK).split('.')[-1] == 'CLK':
            #     year = int(str(CLK).split('WUM0MGXULA_')[-1][0:4])
            #     doy = int(str(CLK).split('WUM0MGXULA_')[-1][4:7])
            #     hour = int(str(CLK).split('WUM0MGXULA_')[-1][7:9])
            #     [gpsweek, gpsweekD] = doy2gpswd(year, doy)
            #     hourFile = 'hour' + str(gpsweek) + str(gpsweekD) + '_' + '%02d' % (hour) +  ".clk"
            #     hourFile = os.sep.join([wdPath, hourFile])
            #     os.rename(CLK, hourFile)
            if 'igs' in str(CLK) and str(CLK).split('.')[-1] == 'clk':
                gpswd = int(str(CLK).split('igs')[-1][0:5])
                for hour in range(0, 24):
                    hourFile = 'hour' + str(gpswd) + '_' + '%02d' % (hour) +  ".clk"
                    hourFile = os.sep.join([wdPath, hourFile])
                    shutil.copy(CLK, hourFile)