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

#
#
# ### 학습목표
#  2. Lambda 함수 이해 및 사용

# * **Lambda 함수**
#  + 단일문으로 표현되는 익명함수
#  + 익명함수란 이름이 없는 구현체만 존재하는 간단한 함수를 의미
#  + 코드 상에서 한번만 사용되는 기능이 있을 때, 굳이 함수로 만들지 않고 1회성으로 만들어서 쓸 때 사용.

# +
def square2(x):
    return x**2

square2(5)
# -

square = lambda x:x**2
square(5)


# +
def add(x, y):
    return x + y

add2 = lambda x,y:x+y
add2(10, 20)


# +
def str_len(s):
    return len(s)

str_len('goods')

# +
strings = ['bob', 'charles', 'alexander3', 'teddy']
# strings.sort(key=str_len)
strings.sort(key=lambda s:len(s))

print(strings)


# -

# #### **filter, map, reduce**
#  + lambda가 유용하게 사용되는 3가지 대표적 함수
#  + 함수형 프로그래밍의 기본 요소이기도 함
#  + filter : 특정 조건을 만족하는 요소만 남기고 필터링
#  + map    : 각 원소를 주어진 수식에 따라 변형하여 새로운 리스트를 반환
#  + reduce : 차례대로 앞 2개의 원소를 가지고 연산. 연산의 결과가 또 다음 연산의 입력으로 진행됨. 따라서 마지막까지 진행되면 최종 출력은 한개의 값만 남게 됨

# +
def even(n):
    return n % 2 == 0

even(3)

# +
nums = [1, 2, 3, 6, 8, 9, 10, 11, 13, 15]

list(filter(lambda n:n%2==0, nums))
# -

# map
# 주어진 리스트, 리스트의 제곱을한 숫자로 새로운 리스트
nums = [1, 2, 3, 6, 8, 9, 10, 11, 13, 15]
list(map(lambda n:n**2, nums))


list(map(lambda n:n%2==0, nums))

# +
import functools

a = [1, 3, 5, 8]
# 리스트 내의 모든 숫자의 합

functools.reduce(lambda x,y:x*y, a)


# -

#
# #### 함수 연습문제
#  1. 주어진 숫자 리스트의 평균을 구하는 함수를 출력하시오
#  1. 해당 숫자가 소수인지 아닌지 판별하시오.
#  2. 2부터 해당 숫자사이에 소수가 몇개인지 출력하는 함수를 구하시오 

# +
# 입력: 숫자 리스트
# 출력: 숫자 리스트의 평균값

def mean(nums):
    # sum 내장 함수로 대체 가능
#     _sum = 0
#     for i in nums:
#         _sum += i
    
    return sum(nums) / len(nums)

print(mean([1, 2, 3]))
print(mean([1, 2, 3, 4, 5]))
print(mean([1, 2, 3.0, 3.9, 8.7]))


# +
# 소수 판별 (1과 자기 자신으로만 나눠지는 수)
# 입력: 양의 정수 1개
# 출력: boolean (소수: True, 합성수: False)

# 16
# 2, 3, 4, 5, 6, 7, 8, .... 15
def is_prime(num):
    for i in range(2, num):
        if num % i == 0: # 나눠 떨어지면 
            return False
    return True  
    
print(is_prime(100))
print(is_prime(89))
print(is_prime(17))
print(is_prime(2))


# +
# 2, 3, 4, 5, 6, 7 -> 4
# 2, 3, 4, 5 -> 3
# 입력: 양의 정수 1개
# 출력: 2-해당 숫자 사이의 소수의 개수

def num_prime(num):
    count = 0
    for i in range(2, num+1):
        if is_prime(i):
            count += 1
    return count

print(num_prime(7))
print(num_prime(5))
print(num_prime(100))
# -








