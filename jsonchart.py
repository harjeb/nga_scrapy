#-*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
import matplotlib
import time, os
from operator import itemgetter

def yestdf(jsonfile):
    datafile = pd.DataFrame(pd.read_json(jsonfile))
    timenow = int(time.time())
    yesttime = timenow - 86400
    datafile2 = datafile.loc[(datafile['posttime'] < timenow) & (datafile['posttime'] > yesttime)]
    return datafile2

def titleCount(df):
    countpa = df.groupby('postarea')['posttitle'].count()
    top = countpa.loc[(countpa.values>0) & (countpa.index != '')]
    top = top.sort_values(ascending=False).ix[0:15]  #按降序取最高的N项
    top.plot(kind='bar')
    ax = plt.gca()
    #ax.set_xticklabels(top.index,rotation=0)  #X坐标轴字体不旋转
    plt.title(u'24H内主题前15板块', fontsize=13)
    plt.show()


def postCount(df):
    dict = {}
    for index,row in df.iterrows():
        if row['postarea'] in dict:
            dict[row['postarea']] = row['postnum'] + dict[row['postarea']]
        else:
            dict[row['postarea']] = row['postnum']
    sd = Series(dict.values(),index=dict.keys())
    sd = sd.loc[(sd.index != '')].sort_values(ascending=False).ix[0:15]
    sd.plot(kind='bar')
    plt.title(u'24H内各版块回帖数', fontsize=14)
    plt.show()

def timeCount(df):
    timedict = {'00-02':0, '02-04':0, '04-06':0, '06-08':0, '08-10':0,
                '10-12':0, '12-14':0, '14-16':0, '16-18':0, '18-20':0,
                '20-22':0, '22-00':0}
    for index,row in df.iterrows():
        time_local = time.localtime(row['posttime'])
        hm = int(time.strftime("%H%M",time_local))
        if 200>=hm and hm>0:
            timedict['00-02'] += 1
        elif 400>=hm and hm>200:
            timedict['02-04'] += 1
        elif 600>=hm and hm>400:
            timedict['04-06'] += 1
        elif 800>=hm and hm>600:
            timedict['06-08'] += 1
        elif 1000>=hm and hm>800:
            timedict['08-10'] += 1
        elif 1200>=hm and hm>1000:
            timedict['10-12'] += 1
        elif 1400>=hm and hm>1200:
            timedict['12-14'] += 1
        elif 1600>=hm and hm>1400:
            timedict['14-16'] += 1
        elif 1800>=hm and hm>1600:
            timedict['16-18'] += 1
        elif 2000>=hm and hm>1800:
            timedict['18-20'] += 1
        elif 2200>=hm and hm>2000:
            timedict['20-22'] += 1
        elif 2400>=hm and hm>2200:
            timedict['22-00'] += 1
    sd = Series(timedict.values(), index=timedict.keys())
    sd.plot(kind='bar')
    plt.title(u'24H内各时间段回帖数', fontsize=14)
    plt.show()






def scrapytoshow():
    if os.path.exists(jsonfile):
        os.remove(jsonfile)
    os.system('scrapy crawl nga -o new.json > log.txt')
    postCount(df)
    titleCount(df)
    timeCount(df)

if __name__ == '__main__':
    jsonfile = 'new.json'
    df = yestdf(jsonfile)
    #titleCount(df)
    #postCount(df)
    #timeCount(df)
    scrapytoshow()
