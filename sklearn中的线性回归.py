# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 09:24:45 2022

@author: zhy
"""

import numpy as np
X=np.array([150,153,154,155,156,157,158,159,160,162,164,166])
X=X.reshape(-1,1)
print(X)
y=np.array([93,93,95,96,98,97,96,98,99,100,102,104])
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X,y)  
print(lr.intercept_,lr.coef_)      	#输出截距和权重系数
new_X=np.array([167,175])
new_X=new_X.reshape(-1,1)
print("两位同学腿长的预测值:",lr.predict(new_X))
