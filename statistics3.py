#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 23:56:09 2021

@author: whso
"""
import math as mt
import numpy as np
import matplotlib.pyplot as plt
man = [140, 145, 160, 190, 155, 165, 150, 190, 195, 138,
                160, 155, 153, 145, 170, 175, 175, 170, 180, 135,
                170, 157, 130, 185, 190, 155, 170, 155, 215, 150,
                145, 155, 155, 150, 155, 150, 180, 160, 135, 160,
                130, 155, 150, 148, 155, 150, 140, 180, 190, 145,
                150, 164, 140, 142, 136, 123, 155]
n = len(man)
x = np.array(man)
plt.hist(x,20)
plt.show()
         

exp_mean = []
for i in range(10000):
    sample = []
    for j in range(n):
        r = np.random.randint(n)
        sample.append(x[r])
    s = np.array(sample)
    exp_mean.append(s.mean())

plt.hist(exp_mean, 50, color='w', edgecolor='black' )
plt.show()

X_ = np.mean(man)
X_std = np.std(man)
print("mean = {0:4.2f}".format( X_))
print("min = {0:4.2f}".format(X_ - 1.96 * X_std / mt.sqrt(n)))
print("max = {0:4.2f}".format(X_ + 1.96 * X_std / mt.sqrt(n)))

    
    
    