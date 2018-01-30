# -*- coding: utf-8 -*-

#计算数据集总的熵（信息量），即数据集的无序程度
from math import log
def calcShannonEnt(dataSet):
    numEntries = len(dataSet) #计算数据集中实例的总数
    labelCounts = {} #创建数据字典
    for featVec in dataSet:
        currentLabel = featVec[-1]  #要导出数据集的label项，就得for循环
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*log(prob,2)
    return shannonEnt


def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels


#按照给定特征划分数据集
def splitDataSet(dataSet,axis,value):  #axis:第几个特征，value：这个特征的值
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec) 
    return retDataSet






















