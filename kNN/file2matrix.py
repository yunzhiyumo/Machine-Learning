# -*- coding: utf-8 -*-


from numpy import *         
import operator #本模块主要包括一些Python内部操作符对应的函数。这些函数主要分为几类：对象比较、逻辑比较、算术运算和序列操作。

# 数据预处理
def file2matrix(filename):
    fr = open(filename) #open()是python的函数
    arrayOLines = fr.readlines() #读取所有行，按行读入
    numberOfLines = len(arrayOLines) #返回行数
    returnMat = zeros((numberOfLines,3)) #建立符合格式的空矩阵
    classLabelVector = [] #建立符合格式的空列表
    index = 0
    for i in arrayOLines:
        i = i.strip() #去掉前后空格字符
        listFromLine = i.split('\t') #split切片 \t制表符
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))  #列表[-1]为倒数第一个，append在list末尾添加新对象
        index += 1
    return returnMat,classLabelVector
