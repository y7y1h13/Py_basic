# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## 학습목표
#  * 반복문의 이해 및 활용 (while)

# ### loop (반복문)
#  + 반복적인 작업을 가능하게 해주는 도구
#  + 특정 조건을 만족하는 경우 수행할 수 있음 (while)
#  + 리스트, 문자열, 튜플 등 컬렉션 타입의 아이템을 하나씩 순회하면서 사용 가능 (for)
#  + 코드 작업에서, 가장 많이 사용하는 구문 중 하나
#  + 주의할점: while을 사용할 경우, 반복을 멈추게 하는 장치가 필요
#    + 그렇지 않으면 셀이 무한히 수행되며, jupyter notebook의 재부팅이 필요

# #### while 키워드
#   - while 뒤의 조건이 True일 경우, while 코드 블록을 계속 수행
#   - while 코드 블록
#     - if와 마찬가지로 while문 아래의 들여쓰기로 작성 된 부분을 의미
#   - 조건이 False가 되면 블록 수행을 멈추고 이후 코드를 실행

# #### while 키워드 이용하여 리스트의 아이템 출력하기

# +
a = [1, 10, 9, 24]

i = 0 # 인덱스
while i < len(a):
    print('value: ', a[i], ', index: ', i)
    i += 1
   
print('hahah')
# -

# #### while 키워드 이용하여 리스트의 아이템 출력하기
#  - 조건문과 함께 사용하기

# +
a = [1, 10, 9, 24, 25, 26]

i = 0 # 인덱스
while i < len(a):
    if a[i] > 20: # 20보다 큰 경우만 출력하기
        print(a[i])
    i += 1
   

# +
a = [1, 10, 9, 24, 25, 26]

i = 0 # 인덱스
while i < len(a):
    if a[i] % 2: # 홀수인 경우만 출력하기
        print(a[i])
    else:
        print(a[i] / 2)
    i += 1
# -

# #### 무한루프
#  - while의 경우 종료가 되지 않도록 코드를 작성하면 블록에서 빠져나올 수 없음

while True:
    print('haha')

# #### break 
#  + loop를 중단할 때 사용
#  + 보통 조건문 안에서 수행되며, 조건을 만족하는 경우 loop를 탈출하기 위해 사용
#  + loop를 중단 하는 경우, while 이후의 코드를 수행

# +
a = [1, 10, 9, 24, 25, 26]

i = 0
while i < len(a):
    if a[i] > 20:
        break
        
    print(a[i])
    
    i += 1
    
print('hahah')
# -

while True:
    data = crawl()
    if data == None:
        break
    print(data)
    

# #### continue
#  + break 처럼 반복을 중단하진 하여 빠져나오지 않고, 다시 while조건으로 점프함
#  + 특정한 경우에는 코드를 수행하지 않고 다음으로 건너 뛰기 위해 사용

a = 7
while a > 0:
    a -= 1
    if a == 5:
        continue
    print(a)

# ### 1 - 100까지 더하기

# +
num = 1
_sum = 0

while num <= 10:
    _sum += num
    num += 1
    print(_sum, num)
    
print(_sum)
# -








