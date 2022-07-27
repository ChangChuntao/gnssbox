#!/usr/bin/python3
# coding=utf-8
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# gnssTime       : GNSS time conversion
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.05
# Latest Version : 2022.06.05 - Version 1.00

# 2022-06-05 : gnss时间转换, 支持['DATETIME', 'YMD', 'YDOY', 'GPSWEEKD', 'MJDSOD']类型的相互转换
#              by Chang Chuntao  -> Version : 1.00
def gnssTimesTran(**kwargs):
    # 传入参数：
    # Time\from\to皆为必选参数
    # Time: 传入的时间，注意传入的格式[支持类型]，例如：time = [2022, 6, 5]
    # From: 传入的时间类型，例如：from = "YMD"
    # To  : 传出的时间类型，例如：to = "GPSWEEKD"
    # 传出参数：
    # outtime：指定类型的时间
    # 支持类型：
    # 1. DATETIME     : python datetime类, datetime(), len = 1
    # 2. YMD          : 年月日, [int, int, int], len = 3
    # 3. YDOY         : 年年积日, [int, int], len = 2
    # 4. GPSWEEKD     : GPS周、GPS周内天, [int, int], len = 2
    # 5. MJDSOD       : 简化儒略日、天内秒, [int, float], len = 2
    import sys
    import datetime
    # 检测传参的正确性
    if 'Time' in kwargs:
        # inTime为传入的时间
        inTime = kwargs['Time']
    else:
        print('未传入时间参数!')
        sys.exit()
    if 'From' in kwargs:
        # fromTime为传入时间类型
        fromTime = kwargs['From']
    else:
        print('需传入需要转换的时间格式!')
        sys.exit()
    if 'To' in kwargs:
        # toTime为传出的时间类型
        toTime = kwargs['To']
    else:
        print('需传入需要传出的时间格式!')
        sys.exit()
    # timeStyle为支持的时间类型
    timeStyle = ['DATETIME', 'YMD', 'YDOY', 'GPSWEEKD', 'MJDSOD']
    # timeStyleLen为支持时间类型的长度，与timeStyle一一对应
    timeStyleLen = [1, 3, 2, 2, 2]

    # 1. 首先将传入的时间格式转换为datetime，转为inDatatime
    if fromTime == 'DATETIME':
        # 判断是否为datetime类型
        if isinstance(inTime, datetime.datetime):
            # 当传入的时间格式即为datetime时，inDatatime直接为inTime
            inDatatime = inTime
        else:
            print('当需转换的时间为datetime时,传入的时间必须为datetime格式!')
            sys.exit()
    else:
        # 判断传入的时间格式长度是否正确
        if len(inTime) != timeStyleLen[timeStyle.index(fromTime)]:
            print('传入的时间格式有误')
            sys.exit()
        else:
            # 将gnss时间转为datetime
            inDatatime = gnssTime2datetime(inTime, fromTime)

    # 2. 后将转出的datetime，转换为指定的时间格式
    if toTime == 'DATETIME':
        # 若传出的时间格式为datetime，调用gnssTime2datetime
        outTime = gnssTime2datetime(inDatatime, toTime)
    else:
        # 若传出的时间格式为gnssTime，调用datetime2gnssTime
        outTime = datetime2gnssTime(inDatatime, toTime)
    return outTime


# 2022-04-30 : GNSS TIME转datetime
#              by Chang Chuntao  -> Version : 1.00
def gnssTime2datetime(gnssTime, gnssTimeType):
    import datetime
    import sys
    if gnssTimeType == "YMD":
        dateTime = datetime.datetime(int(gnssTime[0]), int(gnssTime[1]), int(gnssTime[2]), 0, 0, 0, 0)
    elif gnssTimeType == "YDOY":
        day1Time = datetime.datetime(int(gnssTime[0]), 1, 1, 0, 0, 0, 0)
        dateTime = day1Time + datetime.timedelta(days=int(gnssTime[1]) - 1)
    elif gnssTimeType == "GPSWEEKD":
        wd1Time = datetime.datetime(year=1980, month=1, day=6)
        dateTime = wd1Time + datetime.timedelta(weeks=int(gnssTime[0])) + datetime.timedelta(days=int(gnssTime[1]))
    elif gnssTimeType == "MJDSOD":
        mjdT0 = datetime.datetime(1858, 11, 17, 0, 0, 0, 0)
        dateTime = mjdT0 + datetime.timedelta(days=int(gnssTime[0])) + datetime.timedelta(seconds=float(gnssTime[1]))
    elif gnssTimeType == 'DATETIME':
        dateTime = gnssTime
    else:
        print("暂不支持此格式!")
        sys.exit()
    return dateTime


# 2022-04-30 : datetime转GNSS TIME并输出
#              by Chang Chuntao  -> Version : 1.12
def datetime2gnssTime(specTime, gnssTimeType):
    import datetime
    import sys
    if gnssTimeType == "YMD":
        outTime = [specTime.year, specTime.month, specTime.day]
    elif gnssTimeType == "YDOY":
        delTime = specTime - datetime.datetime(year=specTime.year, month=1, day=1)
        doy = delTime.days + 1
        outTime = [int(specTime.year), doy]
    elif gnssTimeType == "GPSWEEKD":
        gpsWeekdDelTime = specTime - datetime.datetime(year=1980, month=1, day=6)
        gpsWeek = gpsWeekdDelTime.days // 7
        gpsWeekD = gpsWeekdDelTime.days - gpsWeek * 7
        outTime = [gpsWeek, gpsWeekD]
    elif gnssTimeType == "MJDSOD":
        mjdT0 = datetime.datetime(1858, 11, 17, 0, 0, 0, 0)  # 简化儒略日起始日
        mjd = (specTime - mjdT0).days
        sod = specTime.hour * 3600.0 + specTime.minute * 60.0 + specTime.second + specTime.microsecond / 1000000.0
        outTime = [int(mjd), sod]
    else:
        print("暂不支持此格式!")
        sys.exit()
    return outTime


def ymd2doy(year, month, day):
    [year, doy] = gnssTimesTran(From = 'YMD', To = 'YDOY', Time = [year, month, day])
    return year, doy

def ymd2gpswd(year, month, day):
    [gpsWeek, gpsWeekD] = gnssTimesTran(From = 'YMD', To = 'GPSWEEKD', Time = [year, month, day])
    return gpsWeek, gpsWeekD

def ymd2mjd(year, month, day):
    [mjd, sod] = gnssTimesTran(From = 'YMD', To = 'MJDSOD', Time = [year, month, day])
    return mjd, sod

def doy2ymd(year, doy):
    [year, month, day] = gnssTimesTran(From = 'YDOY', To = 'YMD', Time = [year, doy])
    return year, month, day

def doy2gpswd(year, doy):
    [gpsWeek, gpsWeekD] = gnssTimesTran(From = 'YDOY', To = 'GPSWEEKD', Time = [year, doy])
    return gpsWeek, gpsWeekD

def doy2mjd(year, doy):
    [mjd, sod] = gnssTimesTran(From = 'YDOY', To = 'MJDSOD', Time = [year, doy])
    return mjd, sod

def gpswd2ymd(gpsWeek, gpsWeekD):
    [year, month, day] = gnssTimesTran(From = 'GPSWEEKD', To = 'YMD', Time = [gpsWeek, gpsWeekD])
    return year, month, day

def gpswd2doy(gpsWeek, gpsWeekD):
    [year, doy] = gnssTimesTran(From = 'GPSWEEKD', To = 'YDOY', Time = [gpsWeek, gpsWeekD])
    return year, doy

def gpswd2mjd(gpsWeek, gpsWeekD):
    [mjd, sod] = gnssTimesTran(From = 'GPSWEEKD', To = 'MJDSOD', Time = [gpsWeek, gpsWeekD])
    return mjd, sod

def mjd2ymd(mjd, sod):
    [year, month, day] = gnssTimesTran(From = 'MJDSOD', To = 'YMD', Time = [mjd, sod])
    return year, month, day

def mjd2doy(mjd, sod):
    [year, doy] = gnssTimesTran(From = 'MJDSOD', To = 'DOY', Time = [mjd, sod])
    return year, doy

def mjd2gpswd(mjd, sod):
    [gpsWeek, gpsWeekD] = gnssTimesTran(From = 'MJDSOD', To = 'GPSWEEKD', Time = [mjd, sod])
    return gpsWeek, gpsWeekD
