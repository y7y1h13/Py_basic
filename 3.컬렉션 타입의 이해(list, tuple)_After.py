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
#  1. list, tuple에 대해 이해 및 실습
#

# ### **리스트 & 튜플**
#  * 복수개의 값을 담을 수 있는 데이터 구조
#  * 실생활에서 사용하는 리스트(학생 리스트, 성적 리스트 등등)과 동일한 의미로 이해
#  * list - mutable    (생성된 후에 변경 가능)  
#  * tuple - immutable (생성된 후에 변경 불가능)  

# #### **리스트 초기화**
#  - [] 안에 값을 담아서 생성
#  - list() 함수로 생성
#  - str.split()함수로 생성

a = []
print(a)

a = [1, 2, 3, 5, 10]
print(a)

a = ['korea', 'canada', 1, 23, [34, 56]]
print(a)

# * **list() 함수**
#  + 다른 데이터 타입을 리스트로 변환할 때도 사용

# +
a = 'hello world'
b = list(a)
print(b)

c = (1, 2, 3)
d = list(c)

print(d)

# + **string split 함수**
#  * 구분자로 구분되는 리스트를 반환 (빈번히 사용 됨)

# +
a = 'hello world nice weather'
b = a.split()

print(b)
# -

# #### **리스트 indexing**
#  * 문자열의 인덱싱과 동일하게 동작
#  * [] 연산자를 이용하여 항목 얻어오기
#  * [i] - i번째 원소를 반환
#  * i가 음수인 경우도 가능하며 마지막원소가 -1로 하여 앞으로 갈때마다 1씩 감소함

a = [1, 2, 3, 4, 5, 6]
print(a[2])
print(a[5])
print(a[-1])

# #### **리스트 개별 아이템에 접근**
#  - 인덱스에 접근하여 값을 업데이트 가능

# +
# 불변(immutable)
a = 'hello world'
print(a[0])

b = 'jello world'
c = 'j' + a[1:]

d = a.replace('h', 'j')
print(d)
print(a)


# +
a = [1, 2, 3, 4, 5]
a[0] = 100
a[-1] = 90

print(a)
# -

# #### **리스트 slicing**
#  - 문자열 슬라이싱과 동일하게 동작
#  - 슬라이싱의 결과 역시 list!

# +
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[4:7])
print(a[:7])
print(a[3:])
print(a[:])

# slicing 
# start:end:increment(1)

a[1:7]
# -

# ### list 멤버 함수
#  - 생성된 리스트 객체에 동작하는 함수
#  - 향후, 클래스와 멤버 함수 개념을 이해할 예정

# * **append()**
#  + 리스트의 끝에 항목을 추가함

# +
a = [1, 2, 3, 4, 5]
a.append(10)

print(a)

# + **extend()**
#  * 리스트를 연장
#  * += 로도 가능함

# +
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a.extend(b)
a += b
print(a)

# + **insert()로 항목추가**
#  * 리스트의 원하는 위치에 추가 가능
#  * 앞에 인덱스를, 뒤에 아이템을 명시

# +
a = [1, 3, 4, 5, 6]
a.insert(1, 40)

print(a)

# + **remove()**
#  * 값으로 항목 삭제

a = [1, 2, 30, 30, 4, 5]
a.remove(9)
print(a)

# + **pop()**
#   - 지우고자 하는 아이템을 반환 후, 삭제

# +
a = [1, 2, 3, 4, 5]
d = a.pop(2)

print(a)
print(d)

# + **index()**
#  * 찾고자 하는 값의 인덱스 반환

a = [2, 6, 7, 9, 10]
a.index(9)

# * **in 키워드**
#  + 리스트 내에 해당 값이 존재하는지 확인
#  + value in [list]
#  + True, False 중 한가지로 반환

# +
a = [1, 2, 3, 4, 5, 10]
b = 10

c = b in a # False

print(c)

# -

# * **list 정렬**
#  + sort() -> 리스트 자체를 내부적으로 정렬
#  + sorted() -> 리스트의 정렬된 복사본을 반환

a = [9, 10, 7, 19, 1, 2, 20, 21, 7, 8]
a.sort(reverse=True)
b = sorted(a)
print(a)
print(b)

# ### **tuple**
#  - 리스트와 같이 복수개의 값을 갖는 컬렉션 타입
#  - 생성된 후 변경이 불가능

# +
a = [1, 2, 3]
b = (1, 2, 3)

print(type(a))
print(type(b))

a[0] = 100
print(a)

b[0] = 100
print(b)
# -

# #### **tuple unpacking**
#  - 튜플의 값을 차례대로 변수에 대입

a, b, c, d = 100, 200, 300, 400
print(a, b, c, d)

# * **연습문제** a와 b의 값을 교환하시오

# +
a = 5
b = 4

print(a, b)

# # logic
# temp = a
# a = b
# b = temp
a, b = b, a

print(a, b)
# -


