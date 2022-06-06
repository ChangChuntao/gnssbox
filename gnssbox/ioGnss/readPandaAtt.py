#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# readPandaAtt   : Read the Panda Att File
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.05
# Latest Version : 2022.06.05 - Version 1.00

def readPandaAtt(attFile):
    from gnssbox.module.pandaAttClass import pandaAtt
    attFileLine = open(attFile, 'r+').readlines()
    firstLine = attFileLine[0][:-1]
    pandaAttData = []
    count = 0
    for line in attFileLine:
        if line[0] != '%' and line[0] != '#':
            print(line.split())
            mjd = int(line.split()[0])
            sod = float(line.split()[1])
            roll = float(line.split()[2])
            pitch = float(line.split()[3])
            yaw = float(line.split()[4])
            print(len(line.split()))
            if len(line.split()) == 6:
                modeValues = 0.00
                mode = int(line.split()[5])
            else:
                modeValues = float(line.split()[5])
                mode = int(line.split()[6])
            pandaAttData.append(count)
            pandaAttData[count] = pandaAtt(mjd, sod, roll, pitch, yaw, modeValues, mode)
            count += 1
    return firstLine, pandaAttData