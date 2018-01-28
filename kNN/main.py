# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt

if __name__ == '__main__':
    #一、数据预处理，输入文件，输出训练集和label集           
    a,b = file2matrix('e:\\datingTestSet2.txt')
    #二、训练集归一化
    a1 = autoNorm(a)
    
    #三、数据可视化
    d = plt.figure()
    # 0:飞行  1：游戏   2：冰激淋
    e = d.add_subplot(221) #画布的位置
    e.scatter(a1[:,0],a1[:,1],15.0*array(b),15.0*array(b))
    e = d.add_subplot(222)
    e.scatter(a1[:,0],a1[:,2],15.0*array(b),15.0*array(b))
    e = d.add_subplot(223)
    e.scatter(a1[:,1],a1[:,2],15.0*array(b),15.0*array(b))
    plt.show()
    
    #四、kNN预测一个人
    c = kNN([40000,8.5,0.8],a1,b,3)
    print(c)
    
    #五、建立输入界面
    a = classifyPerson(a1,b)
    
    #六、算法错误率
    f = datingClassTest(a1,b)
    print(f)
    