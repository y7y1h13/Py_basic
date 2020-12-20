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
#  1. dictionary, set에 대해 이해 및 실습
#

# ### **dictionary**
#  + 키와 값을 갖는 데이터 구조
#  + 키는 내부적으로 hash값으로 저장
#  + 순서를 따지지 않음. 즉, 인덱스가 없음

a = {'Korea': 'Seoul', 
     'Canada': 'Ottawa', 
     'USA': 'Washington D.C'}
b = {0:1, 1:6, 7:9, 8:10}
print(b[2])

# + **항목 추가 및 변경**
#  - 기존에 키가 존재 하면, 새로운 값으로 업데이트
#  - 존재하지 않으면, 새로운 키, 값 생성

# +
a = {'Korea': 'Seoul', 
     'Canada': 'Ottawa', 
     'USA': 'Washington D.C'}

a['Japan'] = 'Tokyo'
a['Japan'] = 'Kyoto'
a['Japan2'] = 'Kyoto'
a['China'] = 'Beijing'

print(a)

# + **update()**
#  * 두 딕셔너리를 병합함
#  * 겹치는 키가 있다면 parameter로 전달되는 키 값이 overwrite된다.

# +
a = {'a': 1, 'b': 2, 'c' : 3}
b = {'a': 2, 'd': 4, 'e': 5}

a.update(b)

print(a)
# -

# * **key삭제**
#  - del 키워드 사용
#  - pop 함수 이용

# +
a = {'a': 1, 'b': 2, 'c' : 3}
print(a)

# a.pop('b')
del a['b']
print(a)
# -

# * **clear()**
#  + 딕셔너리의 모든 값을 초기화
#

print(a)
a.clear()
print(a)

# * **in**
#  + key값 존재 확인
#  + O(1) 연산 - 딕셔너리의 크기와 관계없이 항상 연산의 속도가 일정하다는 의미

# +
a = {'a': 1, 'b': 2, 'c' : 3}
b = [1, 2, 3, 4, 5, 6, 7, 9, 10, 100]

print(100 in b)
print(2 in a)
# -

# * **value access**
#  + dict[key]로 접급, 키가 없는 경우 에러 발생 
#  + .get() 함수로 접근, 키가 없는 경우 None반환

# +
print(a.get('d'))
# print(a['d'])

if 'd' in a:
    print(a['d'])
# -

# #### **모든 keys, values 접근**
#  + keys() - 키만 반환
#  + values() - 값만 반환
#  + items() - 키, 값의 튜플을 반환

# +
print(a)
print(list(a.keys()))
print(list(a.values()))

list(a.items())
# -

# ### **set**
#  + dictionary에서 key만 활용하는 데이터 구조로 이해
#  + 수학에서의 집합과 동일한 개념

a = {1, 1, 2, 3, 3, 4, 1, 5}
print(a)

# * **set()으로 집합으로 변환**

# +
a = [1, 1, 2, 3, 3, 4, 1, 5]
print(a)

b = set(a)
print(b)

# + **set operations**
#  - 수학 연산과 동일
#  - 교집합, 합집합, 차집합 등 지원

# +
a = {1, 2, 3}
b = {2, 3, 4}

print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a.difference(b)) # 차집합
print(a.issubset(b)) #부분 집합
