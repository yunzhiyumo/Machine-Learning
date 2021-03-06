from numpy import *         
#和import numpy不一样，如果是后者，则需要numpy.array（）
import operator
# =============================================================================
# 测试数据
# def createDataSet():
#     group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
#     labels = ['A','A','B','B']
#     return group,labels
# =============================================================================

# kNN算法：
def kNN(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  #求样本个数
# =============================================================================
# shape函数用法：
# a.shape求数组维度 得到（4L，2L）
# a.shape[0] 为列数
# a.shape[1] 为维度
# =============================================================================
    #以下使用欧式距离公式，共4行
    # 把inX变成4列，再求和dataSet的差
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    # tile（a,（b,2）） 重复数组a，b次,2组组成新的一组
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    # 数组每一行自己相加
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()     
    # argsort函数返回的是数组值从小到大的索引值，是序号
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# =============================================================================
# if __name__ == "__main__":
#     a,b = createDataSet() 
#     c = classify0([0,3],a,b,3)
#     print(c)
# =============================================================================
# =============================================================================
# 如果没有写主函数，那么在python.exe中这样执行：
# 输入 a,b = createDataSet()  
# 输入 classify0([0,0],a,b,3)
# =============================================================================
