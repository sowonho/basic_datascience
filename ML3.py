# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:32:34 2021

@author: user
"""
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

print("상관계수 r = ", r)
speed = myfunc(10)
print("등록 기록: {0:3d} -> 예측 통과 속도: {1:3.1f}".format(10, speed))

mymodel = list(map(myfunc, x))  # x값에 대응하는 예측 y값 계산
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.plot(10, speed, marker = 'D', ms = 10, color = 'red')
plt.show()
