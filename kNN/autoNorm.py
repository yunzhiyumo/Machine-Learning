# -*- coding: utf-8 -*-

from numpy import *         

#数据归一化
def autoNorm(dataSet):
    minVals = dataSet.min(0) #选取矩阵每列的最小值
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))   #shape复制了dataSet整体结构
    m = dataSet.shape[0]  #dataSet结构中的一部分
    normDataSet = (dataSet - tile(minVals,(m,1)))/tile(ranges,(m,1))
    return normDataSet
    