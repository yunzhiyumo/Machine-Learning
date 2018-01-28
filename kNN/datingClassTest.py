# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:04:00 2018

@author: pm123
"""
#算法错误率
def datingClassTest(normMat,datingLabels):
    hoRatio = 0.05
    m = normMat.shape[0] #数据总数量
    numTestVecs = int(m*hoRatio) #测试集数量
    errorCount = 0.0
    for i in range(numTestVecs):  #前numTestVecs行作为测试集
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "预测值为: %d,真实值为: %d" % (classifierResult,datingLabels[i])
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print "错误率为: %f" % (errorCount/float(numTestVecs))
    
    