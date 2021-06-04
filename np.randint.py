#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 00:31:54 2021

@author: whso
"""

import numpy as np
import matplotlib.pyplot as plt

tries = 100
x = np.random.randint(10, size=(tries))
plt.hist(x,100)
plt.show()