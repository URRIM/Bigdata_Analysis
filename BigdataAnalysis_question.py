# -*- coding: utf-8 -*-
"""빅분기_강의자료_문제

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rSSRFsiGAfQmpIsxe6a1WLjYyoNJ4OOA
"""

# 작업형 유형 1문제(1)
import seaborn as sns
import pandas as pd
sns.get_dataset_names()
df = sns.load_dataset('car_crashes')
print(df.head())

#사용자 코드



# 작업형 유형 1문제(2)
import seaborn as sns
import pandas as pd
import numpy as np
df = sns.load_dataset('planets')
print(df.head())

#사용자 코드



# 작업형 유형 1문제(3)
import seaborn as sns
sns.get_dataset_names()
df = sns.load_dataset('planets')
print(df.head())

# 사용자 코드



# 작업형 유형 2(기초쌓기)

import seaborn as sns
df = sns.load_dataset('penguins')
print(df.head())

#1. 결측치 입력

#2. 라벨인코딩

#3. 데이터 변환, 더미

#4. 파생변수

#5. 스케일

#6. 데이터 분리

#7. 모형학습



#8. 앙상블

#9. 모형평가

#10. 하이퍼파라미터 튜닝

#11. 파일저장



#연습문제1
#- 성능이 우수한 예측모형을 구축하기 위해서는 적절한 데이터 전처리,
# 피쳐엔지니어링, 분류 알고리즘 사용, 초매개변수 최적화, 모형 앙상블 등이 수반되어야 한다.
#- 수험번호.csv(예:0000.csv) 파일이 만들어지도록 코드를 제출한다.
#- 제출한 모형의 성능은 ROC-AUC 평가지표에 따라 채점한다.
#- predict_proba로 예측, 범주1의 확률을 예측
# 데이터 파일 읽기 예제

import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split

df = sns.load_dataset('titanic')
X_train, X_test, y_train, y_test = train_test_split(df, df['survived'], test_size=0.2, random_state=42, stratify=df['survived'])
X_train = X_train.drop(['alive', 'survived'], axis=1)
X_test = X_test.drop(['alive', 'survived'], axis=1)
print(X_train.head())

#사용자 코드
#1. 결측치 입력

#2. 라벨인코딩

#3. 데이터 변환, 더미

#4. 파생변수

#5. 스케일

#6. 데이터 분리

#7. 모형학습, 8. 앙상블

#9. 모형평가

#10. 하이퍼파라미터 튜닝

#11. 파일저장

#확인



#연습문제2(회귀예측)
#- 성능이 우수한 예측모형을 구축하기 위해서는 적절한 데이터 전처리,
# 피쳐엔지니어링, 분류 알고리즘 사용, 초매개변수 최적화, 모형 앙상블 등이 수반되어야 한다.
#- 수험번호.csv(예:0000.csv) 파일이 만들어지도록 코드를 제출한다.
#- 제출한 모형의 성능은 RMSE, MAE가 평가지표에 따라 채점한다.

# 데이터 파일 읽기 예제
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = sns.load_dataset('mpg')
X_train, X_test, y_train, y_test = train_test_split(df, df['mpg'], test_size=0.2, random_state=42)
X_train = X_train.drop(['mpg'], axis=1)
X_test = X_test.drop(['mpg'], axis=1)
print(X_train.head())

# 사용자 코딩
#1. 결측치 제거

#2. 라벨 인코더

#3. 카테고리 변환, 더미

#4. 파생변수 생성

#5. 스케일 작업

#6. 데이터 분리

#7. 모델 학습

#8.앙상블(스태킹)

#9. 모형평가

#10. 하이퍼파라미터 튜닝

#11. 파일저장

#확인



# KDATA 실습환경
# 출력을 원할 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

# 데이터 파일 읽기 예제
import pandas as pd
a = pd.read_csv('data/mtcars.csv', index_col=0)

# 사용자 코딩


# 답안 제출 예시
# print(평균변수값)

# 출력을 원하실 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

# 데이터 파일 읽기 예제


# 사용자 코딩
#1. 결측치 제거


#2. 라벨 인코더



#3. 카테고리 변환, 더미


#4. 파생변수 생성


#5. 스케일 작업


#6. 데이터 분리

#7. 모형학습, 8. 앙상블


#9. 모형평가


#10. 하이퍼파라미터 튜닝


#11. 파일저장


#확인



# 답안 제출 참고
# 아래 코드 예측변수와 수험번호를 개인별로 변경하여 활용
# pd.DataFrame({'cust_id': X_test.cust_id, 'gender': pred}).to_csv('003000000.csv', index=False)