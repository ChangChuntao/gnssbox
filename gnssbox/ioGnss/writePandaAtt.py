def writePandaAtt(firstLine, newPandaAttData, outPandaAttfile):
    outf = open(outPandaAttfile, 'w')
    outf.write(firstLine + '\n')
    outf.write('%% Time (GPST) Roll (radian) Pitch (radian) Yaw (radian) Flag\n')
    outf.write('%% Start and stop time :' + 
               (str(newPandaAttData[0].mjd)).rjust(9) + 
               ('%.5f' % (newPandaAttData[0].sod)).rjust(15) + 
               (str(newPandaAttData[-1].mjd)).rjust(9) + 
               ('%.5f' % (newPandaAttData[-1].sod)).rjust(15) + '\n')
    outf.write('%% End of header\n')
    for data in newPandaAttData:
        outf.write((str(data.mjd)).rjust(6) + 
                   ('%.5f' % (data.sod)).rjust(13) + 
                   ('%.13f' % (data.roll)).rjust(19) +
                   ('%.13f' % (data.pitch)).rjust(19) +
                   ('%.13f' % (data.yaw)).rjust(19) +
                   ('%.13f' % (data.modeValues)).rjust(19) +
                   (str(data.mode)).rjust(2) + 
                   '\n')