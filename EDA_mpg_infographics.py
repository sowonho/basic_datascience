# -*- coding: utf-8 -*-

# EDA_.py
### 기본 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
[Step 1] 데이터 준비 - read_csv() 함수로 자동차 연비 데이터셋 가져오기
'''
# CSV 파일을 데이터프레임으로 변환
url = "https://raw.githubusercontent.com/sowonho/basic_datascience/master/auto-mpg.csv"
df = pd.read_csv(url)

# horsepower 열의 자료형 변경 (문자열 ->숫자)
print(df['horsepower'].unique())          # horsepower 열의 고유값 확인
print('\n')

df['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)   # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')      # 문자열을 실수형으로 변환

# 분석에 활용할 열(속성)을 선택 (연비, 실린더, 출력, 중량)
ndf = df[['mpg', 'cylinders', 'displacement', 'horsepower', 'weight']]


# Matplotlib으로 산점도 그리기
ndf['mpg'].plot(kind='hist')
plt.show()
plt.close()

ndf[['mpg','cylinders']].plot(kind='box')

ndf.plot(kind='scatter', x='weight', y='mpg',  c='coral', s=10, figsize=(10, 5))
plt.show()
plt.close()

c_size = ndf.cylinders/ndf.cylinders.max() * 300
ndf.plot(kind='scatter', x='displacement', y='mpg', figsize=(10, 5),
         s=c_size, alpha=0.5 )
plt.show()
plt.close()

mpg_size = ndf.mpg/ndf.mpg.max() * 300
ndf.plot(kind='scatter', x='displacement', y='weight', figsize=(10, 5),
          s=mpg_size, alpha=0.5)
plt.show()
plt.close()

# seaborn으로 산점도 그리기
fig = plt.figure(figsize=(10, 5))   
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax1)                 # 회귀선 표시
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax2, fit_reg=False)  #회귀선 미표시
plt.show()
plt.close()

# seaborn 조인트 그래프 - 산점도, 히스토그램
sns.jointplot(x='weight', y='mpg', data=ndf)              # 회귀선 없음
sns.jointplot(x='weight', y='mpg', kind='kde', data=ndf)  # 회귀선 표시
plt.show()
plt.close()

# seaborn pariplot으로 두 변수 간의 모든 경우의 수 그리기
sns.pairplot(ndf)  
plt.show()
plt.close()
mpg_corr = ndf.corr()
print(mpg_corr)

