# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 19:58:06 2021

@author: user
"""

import numpy as np
import pandas as pd

from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = [12, 8]
# Getting Titanic dataset
url = "https://raw.github.com/mattdelhey/kaggle-titanic/master/Data/train.csv"
titanic = pd.read_csv(url)
titanic.info()

# titanic = titanic[['survived', 'pclass', 'sex']]  # 사용할 속성 추출

# titanic["SURVIVE"] = titanic.survived.map({0: "DEAD", 1: "ALIVE"})
# titanic["CLASS"] = titanic.pclass.map({1: "1ST", 2: "2ND", 3: "3RD"})
# titanic["GENDER"] = titanic.sex.map({'male': 'MAN', 'female': "WOMAN"})
# titanic.head()

# mosaic(titanic.sort_values('CLASS'), ['SURVIVE', 'CLASS'], 
#       title='Mosaic Chart of Titanic Survivor')

# plt.show()

