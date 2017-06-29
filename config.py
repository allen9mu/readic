#!/usr/bin/env python  
#coding:utf-8  

import logging

#数据格式  
#第一位：类型，1代表POU中的算法 2代表数据库中的算法
#第二位：类型或关健字，1时为关健字，2时为算法名称
#第三位：第一组 目标点项，参考点项,对应关系及参考值
#第四位：第一组 目标点项，参考点项,对应关系及参考值
#...
#...
#
CONFIG = [[1,'FOI',['OK_1','AV','E']],
          [2,'AMAN1',['TR','RM','R',3,1],['AV_1','AV','E']],
          [2,'AMAN2',['TR','RM','R',3,1],['AV_1','AV','E']],
          [2,'AMAN3',['TR','RM','R',3,1],['AV_1','AV','E']],
          [2,'AMAN4',['TR','RM','R',3,1],['AV_1','AV','E']]
          ]

#IOLIST位置
IOLIST_POS = "E:\\WorkPlace\\ICUPDATE2\\iolist.xlsx"
#IC位置
IC_POS = "E:\\WorkPlace\\ICUPDATE2\\IC"
#临时文件存放
TEMP_POS = "E:\\WorkPlace\\ICUPDATE2\\TEMP"
#输出文件存放
OUTPUT_POS = "E:\\WorkPlace\\ICUPDATE2\\OUTPUT"
#存储IC的号码
IC_NUMBER = '101'


#日志输出开关
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')