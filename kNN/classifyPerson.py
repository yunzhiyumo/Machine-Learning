# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:50:40 2018

@author: pm123
"""
from numpy import *         
import operator
import Tkinter as tk

def classifyPerson(a,b):
    #可视化界面
    w = tk.Tk()
    w.title('my windows')
    w.geometry('200x200')
    
    s = tk.StringVar()
    s.set('game')
    e1 = tk.Entry(w,textvariable=s,show='')
    e1.pack()
    
    e2 = tk.Entry(w,show='')
    e2.pack()

    e3 = tk.Entry(w,show='')
    e3.pack()
    
    
    def insert_point():
        var1 = e1.get()
        var2 = e2.get()
        var3 = e3.get()
        percentTats = float(var1)
        ffMiles = float(var2)
        iceCream = float(var3)
        inArr = array([percentTats,ffMiles,iceCream])
        result = kNN(inArr, a, b, 3)
        resultList = ['not at all','in small doses','in large doses']
        t.insert('insert',resultList[result-1])
        
    b1 = tk.Button(w,text='predict',height='2',width='20',command=insert_point)
    b1.pack()
    
    t = tk.Text(w,height=2)
    t.pack()
# =============================================================================
#     percentTats = float(raw_input('game time:'))
#     ffMiles = float(raw_input('fly distance:'))
#     iceCream = float(raw_input('icecream amount:'))
# =============================================================================
# =============================================================================
#     inArr = array([e1,e2,e3])
#     result = kNN(inArr, a, b, 3)
#     print 'like he?',resultList[result-1]
# =============================================================================
    
    w.mainloop()