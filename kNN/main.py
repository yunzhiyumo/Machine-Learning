# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 13:47:20 2018

@author: pm123
"""
import matplotlib
import matplotlib.pyplot as plt

if __name__ == "__main__":
     a,b = file2matrix('e:\\datingTestSet2.txt')
     c = classify0([40000,8.5,0.8],a,b,20)
     print(c)

     d = plt.figure()
     e = d.add_subplot(111)
     e.scatter(a[:,1],a[:,2])
     plt.show()
     
     