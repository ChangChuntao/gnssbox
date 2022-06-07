#!/usr/bin/python3
# gnssbox        : The most complete GNSS Python toolkit ever
# Github         : https://github.com/ChangChuntao/gnssbox.git
# GetGnssData    : Use FAST software for data download
# Author         : Chang Chuntao 1252443496@qq.com
# Copyright(C)   : The GNSS Center, Wuhan University
# Creation Date  : 2022.06.03
# Latest Version : 2022.06.03 - Version 1.00
# Needed         : FAST Git # https://github.com/ChangChuntao/FAST.git


def GetGnssData(FAST, downloadType, **kwargs):
    # 必传参数
    # FAST        : FAST软件对应的路径，注意bin文件夹与FAST需在同一路径
    # Github      : https://github.com/ChangChuntao/FAST.git
    # downoadType : 下载的数据类型，双击运行FAST软件输入a，按提示查看支持的数据类型，例如："MGEX_brdm"
    # 可选参数，查看FAST文件夹下说明文档，见3.2 引导下载模式，可知各类型所需的参数
    # 需要注意的   : 除P1C1、P1P2、P2C2、IVS_week_snx需要year month外其他数据必选的参数为year doy(或doy1 doy2)
    # year        ：年份，例如：year = 2022
    # doy         : 年积日，例如：doy = 100
    # doy1        : 起始年积日，例如：doy1 = 100
    # doy2        : 截至年积日，例如：doy2 = 103，注意: doy1与doy2需同时传入
    # month       ：特殊类型可用，月份，例如：month = 2
    # path        : 下载目录，例如：path = r'D:\Code\gnssbox\gnssbox\getGnssData\example，默认为程序运行路径
    # unzip       : 是否解压，例如：unzip = False，默认为True
    # sitefile    : 站点名文件，当需要下载站点数据时，为必选传入参数，例如：sitefile = r'D:\Code\gnssbox\gnssbox\getGnssData\example\igs.txt'
    # process     : 下载并发数，例如：process = 6，默认为8
    print()