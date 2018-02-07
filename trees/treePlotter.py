# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 20:25:23 2018

@author: pm123
"""

import matplotlib.pyplot as plt

decisionNode = dict(boxstyle='sawtooth',fc='0.8')
leafNode = dict(boxstyle='round4',fc='0.8')
arrow_args = dict(arrowstyle='<-')

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    #添加注释 annotate()
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',
                            xytext=centerPt,textcoords='axes fraction',
                            va='center',ha='center',bbox=nodeType,arrowprops=arrow_args)
    
def createPlot():
    fig = plt.figure(1,facecolor='white')
    fig.clf() #清空绘图区域
    createPlot.ax1 = plt.subplot(111,frameon=False)
    plotNode('决策节点',(0.5,0.1),(0.1,0.5),decisionNode)
    plotNode('叶子节点',(0.8,0.1),(0.3,0.8),leafNode)
    plt.show()


def getNumLeafs(myTree):
    numleafs = 0
    firstStr = myTree.keys()[0]  #.keys()取出字典中的key值
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])  #递归：无限调用自身这个函数，每次调用总会改动一个关键变量，直到这个关键变量达到边界的时候，不再调用。
        else:
            numLeafs += 1
    return numLeafs
    
def getTreeDepth():
    