# -*- coding: utf-8 -*-


from numpy import *         
import operator

# 数据预处理
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
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