#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 23:56:09 2021

@author: whso
"""

import numpy as np
import matplotlib.pyplot as plt

tries = 100000
x = np.random.binomial(4, 0.2, tries)
plt.hist(x,100)
plt.show()
         
y = np.random.normal(2.0, 1, tries)
plt.hist(y,100)
plt.show()

z = np.random.uniform(0, 3, tries)
plt.hist(z, 100)
plt.show()

exp_mean = []
for i in range(10000):
    sample = []
    for j in range(36):
        r = np.random.randint(100000)
        sample.append(x[r])
    s = np.array(sample)
    exp_mean.append(s.mean())

plt.hist(exp_mean, 50, color='w', edgecolor='black' )
plt.show()
    
    
    