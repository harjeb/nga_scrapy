#-*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
import matplotlib
import time, os

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

def scrapytoshow():
    if os.path.exists(jsonfile):
        os.remove(jsonfile)
    os.system('scrapy crawl nga -o new.json > log.txt')
    postCount(df)
    titleCount(df)

if __name__ == '__main__':
    jsonfile = 'new.json'
    df = yestdf(jsonfile)
    titleCount(df)
    #postCount(df)
    #scrapytoshow()
