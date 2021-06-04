# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:01:04 2021

@author: user
"""

# file name: ex03_1.py

import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()

print(diabetes.data.shape, diabetes.target.shape)

print(diabetes.data[0:3]) # 10 개 속성, 3개 항목

print(diabetes.target[:3]) # 3개 항목에 해당하는 타켓 3개

plt.scatter(diabetes.data[:, 2], diabetes.target)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
