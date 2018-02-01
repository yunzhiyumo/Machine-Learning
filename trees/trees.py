# -*- coding: utf-8 -*-

from math import log
import operator #majorityCnt()

def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels

#计算数据集总的熵 = 分配到不同类别的概率*分配到不同类别产生的熵 求和 ，即数据集的无序程度
def calcShannonEnt(dataSet):
    numEntries = len(dataSet) #计算数据集中实例的总数
    #统计不同label出现的次数，称为投票表决法
    labelCounts = {} #创建数据字典
    for featVec in dataSet:
        currentLabel = featVec[-1]  #yes/no
        if currentLabel not in labelCounts.keys(): 
            labelCounts[currentLabel] = 0 #字典新增一个kv
        labelCounts[currentLabel] += 1
    #return labelCounts = {'yes':2,'no':3}
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries #此label的样本在总样本
        shannonEnt -= prob*log(prob,2)
    return shannonEnt


#按照给定特征划分数据集
def splitDataSet(dataSet,axis,value):  #axis:第几个特征，value：这个特征的值
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]  #把此特征之前的特征保留
            reducedFeatVec.extend(featVec[axis+1:])  #把此特征之后的特征保留
            retDataSet.append(reducedFeatVec)  #extend 把值加入，append 把list加入
    return retDataSet

#选择最大熵的特征的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0])-1  #特征个数
    baseEntropy = calcShannonEnt(dataSet)  #香农信息期望值
    bestInfoGain = 0.0 
    bestFeature = -1
    for i in range(numFeatures):  #遍历所有特征一，二
        featList = [example[i] for example in dataSet] #递推式构造列表，提取dataSet第一个特征所有的值
        uniqueVals = set(featList) #set()函数创建一个无序不重复元素集,去掉列表重复元素
        # 计算每个特征带来的熵（每组数据的熵的加权平均数）
        newEntropy = 0.0
        for value in uniqueVals: #第一个特征的值：0 1
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subDataSet) #2组的熵的加权平均数
        infoGain = baseEntropy - newEntropy
        
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

#求数量最多的特征
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    #排序 iteritems()迭代器，reverse=True降序，
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]  #出来的结果会把字典变成[('C', 10), ('B', 12), ('A', 15)]


def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]  #['yes', 'yes', 'no', 'no', 'no']
    #判断是否只有一个特征
    if classList.count(classList[0]) == len(classList): 
        return classList[0]
    if len(dataSet[0]) == 1:
       return majorityCnt(classList)  
    #else
    bestFeat = chooseBestFeatureToSplit(dataSet) #找出最大熵特征
    bestFeatLabel = labels[bestFeat] #最大熵特征的名称
    myTree = {bestFeatLabel:{}} #一次输出！！  ！
    #为下次循环做准备
    del(labels[bestFeat]) #！！！
    featValues = [example[bestFeat] for example in detaSet] #最优特征的所有值
    uniqueVals = set(featValues) #[0,1]
    for value in uniqueVals:  # 0 1
        subLabels = labels[:]  #{'flippers'}
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree

 

    
