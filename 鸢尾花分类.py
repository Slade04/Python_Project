# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 09:29:42 2022

@author: zhy
"""

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
iris=datasets.load_iris() 			    # 获取鸢尾花数据集
X=iris.data 				    # 获取鸢尾花特征矩阵
y=iris.target  				    # 获取鸢尾花目标数组
knn = KNeighborsClassifier(n_neighbors=3)   # 初始化模型
knn.fit(X,y)   
score=knn.score(X,y)			    # 测试模型
print(score)				
y_sample=knn.predict([[4,3,4,5]])		    # 预测数组
print("KNeighborsClassifier分类器预测结果:{}".format(y_sample))
