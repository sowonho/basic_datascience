# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:32:32 2021

@author: user
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Getting mpg dataset
url = "https://raw.githubusercontent.com/sowonho/basic_datascience/master/auto-mpg.csv"
df = pd.read_csv(url)

print(df.head(10))
print(df.shape)
columns = list(df.columns)
print(columns)
print(df.info())
des = df.describe()
print(des)

