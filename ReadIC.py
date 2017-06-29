#!/usr/bin/env python  
#coding:utf-8  

#读取IC，根据IOLIST的点项清单确认点项，同时根据CONFIG梳理点项清单。

import logging
from config import CONFIG,IC_POS



#'''CSV文件转化为字典''' 
def trans_ic_dict(file):
    ic_dict={}
    filelist = open(file)
    flag =1   
    for line in filelist.readlines():
        if flag ==1 :
            flag=0
            pass
        else:
            line = line.strip("\n")
            list_line=line.split(',')
            key=list_line[0].split('"')
            list1=list_line[1].split('"')
            list2=list_line[2].split('"')

            if len(key)>1:
                A = key[1]
            else:
                A = key[0]            
            
            if len(list1)>1:
                B = list1[1]
            else:
                B = list1[0]
                
            if len(list2)>1:
                C = list2[1]
            else:
                C = list2[0] 
            
                
            ic_dict[A]=[B,C]
    return ic_dict



#建立需在读取的IC中的的清单keys
def get_ic_keys(CONFIG):
    logging.info('开始生成ic keys清单')
    keys = {}
    for i in range(len(CONFIG)):
        list=[]
        if CONFIG[i][0]==1:
            for j in range(2,len(CONFIG[i])):
                list.append(CONFIG[i][j]) 
            keys[CONFIG[i][1]]=list  
    logging.info('结束生成ic keys清单')
    return keys 

#获取站号
def get_ic_SN(file):
    filelist = file.split('.')
    return filelist[0]

#制作IC的点表清单
def get_ic_list(ic_dict, IC_key,points_iolist,SN):
    points ={}
    SNlist = {}
    for key in points_iolist.keys():
        if points_iolist[key][1] == int(SN):
            SNlist[key]=points_iolist[key]
    for name in ic_dict.keys():
        for key in IC_key.keys():
            for i in range(len(IC_key[key])):
                if key in name:
                    if IC_key[key][i][0] in name:
                        n=len(name)-len(IC_key[key][i][0])
                        newname = name [:n]+IC_key[key][i][0]
                        points[newname] = ic_dict[name]
        for key in SNlist.keys():
            if SNlist[key][0] == name:
                if SNlist[key][2]=='E':
                    points[key]=ic_dict[name]                   
                elif SNlist[key][2]=='R' and int(ic_dict[name][1])==3 :
                    points[key] = ['BOOL',1]                
                    
    return points

#制作IC的中IOLIST点表清单
def get_ic_iolist(ic_dict, IOlist_dict):
    points ={}
    for name in ic_dict.keys():
        for key in IOlist_dict.keys():
            if key in name:
                if IOlist_dict[key][0] not in name:
                    #增加一个‘.’， 以便与IC中的点的格式保持一致
                    points['.'+IOlist_dict[key][0]] = ic_dict[name]
                    
def get_ic_iolist_2(ic_dict, IOlist_dict):
    points ={}
    for name in ic_dict.keys():
        for key in IOlist_dict.keys():
            if '.'+key == name:
                newname =name[0:len(name)-2]+'TR'
                points[newname] = ['BOOL',1]
                    
    return points


if __name__ =='__main__':
    print(get_ic_keys(CONFIG))
    
    