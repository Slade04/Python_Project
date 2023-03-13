# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 10:06:43 2022

@author: zhy
"""

import matplotlib.pyplot as plt
import seaborn as sns;sns.set()
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
# 生成模拟的二维数据,默认30个点
X,y = make_blobs(15, random_state=1)
# 画出原始数据集
plt.scatter(X[:,0],X[:,1])
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
y_pred=kmeans.predict(X)
plt.scatter(X[:,0],X[:,1],c=y_pred,cmap='viridis')
plt.show()
