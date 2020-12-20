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
#  * 반복문의 이해 및 활용 (for)
#  * range 함수 이해

# ### for 반복문 
#  - 리스트, 문자열 등등 순회 가능한 객체를 순회하면서 값을 처리할 때 사용
#  - 아래와 같은 문법으로 사용
#  - 여기서 i는 매번 수행 될 때마다, a의 아이템으로 순차적으로 변경 됨
#  - 모든 아이템이 순회되면 for 블록 종료
#  
# ```python
# a = [1, 2, 4, 3, 5]
# for i in a:
#     print (i, i * 2)
# ```

a = [1, 2, 4, 3, 5]
for i in a:
    print (i, i * 2)
print('hahah')

a = [1, 2, 4, 3, 5]
for number in a:
    print(number)
print('hahah')

# #### 문자열의 아이템 출력하기
#  - 문자열의 경우 순회 가능, 리스트의 유사하게 순회 가능

for x in 'hello world':
    print(x)

a = 'hello world'
for character in a:
    print(character)

# #### 리스트 아이템 출력하기

a = [1, 10, 3, 4, 5]
for num in a:
    if num % 2 == 0:
        print(num/2)
    else:
        print(num+1)

# #### dict의 아이템 출력하기
#   - dictionary의 경우 기본적으로 순회 하게 되면 key값을 참조
#   - keys()함수를 이용하여 key 값만 순회 가능
#   - values()함수를 이용하여 value 값만 순회 가능
#   - items()함수를 이용하여 tuple형태로 key, value 순회 가능

a = {'korea': 'seoul', 'japan': 'tokyo', 'canada': 'ottawa'}
for key in a:
    print(key, a[key])

for key in a:
    print(key)

for value in a.values():
    print(value)

list(a.items())

for key, value in a.items():
    print(key, value)

# #### for에서 index 사용하기
#   - 기본적으로 for에 리스트를 순회하는 경우, 값만 추출 함
#   - 아래와 같은 코드로 인덱스와 값 모두 사용 가능(enumerate 함수 이용)
#
# ```python
# a = [1, 2, 4, 3, 5]
# for i, val in enumerate(a):
#     print i, val
# ```

a = [1, 2, 3, 4, 5]
for index, num in enumerate(a):
    if index > 3:
        print(index, num)

# ####  break
#   - for의 경우에도 특정 조건일 때, loop 종료가 가능

a = [100, 90, 80, 70, 60, 50]
for num in a:
    if num < 80:
        break
        
    print(num)

# #### continue
#  - 해당 아이템을 건너 뛰고 싶을 때 사용

a = [100, 90, 80, 70, 60, 50]
for num in a:
    if num >= 60 and num <= 70:
        continue
    print(num)

# #### loop 중첩
#   - 반복문의 경우에도 중첩하여 사용 가능
#   - 중첩이라는 것은 반복문 블록의 코드안에 또 반복문의 코드가 작성되는 것을 의미
#   - 이런 경우, 내부 루프는 외부 루프가 수행되는 만큼 반복 수행 됨
#   - 또한 중첩의 경우 무한히 가능
#
# ```python
# a = [1, 2, 4]
# for i in a:
#     for j in a:
#         print i * j
# ```

a = [1, 2, 4]
for i in a:
    for j in a:
        print(i * j)

# #### 구구단 출력하기

# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# ...
# 2 * 9 = 18
# 3 * 1 = 3
# ..
# 3 * 9 = 27
# ...
# 9 * 1 = 9
# ...
# 9 * 9 = 81

# +
x = [2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in x:
    for j in y:
        print(i, 'x', j, '=', i*j)
        
# -

# #### collection의 길이
#  - len() 내장함수로 계산 가능
#  - 내장함수란 파이썬 내부에 구현되어 있어서, import하지 않고도 사용 가능한 함수를 의미
#  - abs, len, type, range 등이 있음 (과정 진행하면서 필요할 때마다 다룰 예정)

a = [1, 2, 3, 4, 5, 1]
len('hello world')

# #### range 함수
#   - 리스트를 쉽게 만들 수 있는 내장함수
#   - 주어진 값에 따라 다양한 결과를 반환
#  
# ```python
# range(10)       -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(2, 10)    -> [2, 3, 4, 5, 6, 7, 8, 9] 
# range(2, 10, 3) -> [2, 5, 8] 
# ```

# * 1 - 100까지의 리스트 생성하기

list(range(101))

a = list(range(1, 201))
print(a)

list(range(1, 101, 5))

# * **연습문제** 1부터 100사이의 5의 배수만을 갖는 리스트를 생성하시오

list(range(5, 101, 5))

# ### if & for 연습문제
#    
#   1. 구구단을 2 - 9단까지 출력하시오.
#   2. 1 - 100까지 정수 중 2의 배수 또는 11의 배수를 모두 출력하시오. 
#   4. a = [22, 1, 3, 4, 7, 98, 21, 55, 87, 99, 19, 20, 45] 에서 최대값과 최소값을 찾으시오. (sorted, sort 사용 금지)
#   5. a = [22, 1, 3, 4, 7, 98, 21, 55, 87, 99, 19, 20, 45] 에서 평균을 구하세요.
#   

x = 2
while x <= 9:
    y = 1
    while y <= 9:
        print(x, 'x', y, '=', x*y)
        y += 1
    x += 1

nums = list(range(1, 101))
for x in nums:
    if x % 2 == 0 or x % 11 == 0:
        print(x)

# sort 함수(정렬)을 사용한 경우
a = [22, 1, 3, 4, 7, 98, 21, 55, 87, 99, 19, 20, 45]
a.sort()
a[0], a[-1]

# +
# 처음 만나는 값을 최소 값으로 가정
# 그리고 그 후 숫자를 만날때마다 현재 최소값보다 그 숫자가 작으면 최소값을 그 숫자로 업데이트

_min = a[0]
for x in a:
    if x < _min:
        _min = x
print(_min)
        
# -

_max = a[0]
for x in a:
    if x > _max:
        _max = x
print(_max)

# +
# 최대 최소 동시에
_min = a[0]
_max = a[0]
for x in a[1:]:
    if x < _min:
        _min = x
    if x > _max:
        _max = x

print(_min, _max)

# -

a = [22, 1, 3, 4, 7, 98, 21, 55, 87, 99, 19, 20, 45]

# +
# while
i = 0
_sum = 0
while i < len(a):
    _sum += a[i]
    i += 1
    
print(_sum / len(a))
    


# +
# for
_sum = 0
for x in a:
    _sum += x
    
print(_sum / len(a))
    
# -


