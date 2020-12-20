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

# ### 학습목표
#  1. 함수의 이해
#  2. 함수 구현 및 사용 숙지

# ### 함수?
# * 지금까지 무심코 코드에서 사용된 많은 함수들이 존재 합니다.
# * 예를들면, sum, len, range 같은 함수 등이 있죠.
# * 함수란 우리가 알고있는 개념처럼 주어진 입력(input)에 대해서 의도된 출력(output)를 전달하는 역할을 합니다.
#
# * 그렇다면, 하나씩 살펴보겠습니다.
#   > range 함수는 정수를 입력으로 전달하면 [0, 정수) 로 이루어진 리스트를 생성하는 역할을 합니다.
#   
#   > sum 함수는 리스트, 튜플등을 입력으로 전달하면 전체 아이템의 합을 출력으로 전달하는 역할을 합니다.
#   
#   > len 함수는 리스트, 튜플등을 입력으로 전달하면 아이템의 개수를 출력으로 전달하는 역할을 합니다.
#   
# * 그리고, 위의 함수들은 모두 python 내부에 이미 정의(구현)이 되어 있습니다.
# * 위와 같은 함수를 내장함수(built-in function)이라고 합니다.

# +
# 내장 함수의 예
a = [1, 2, 3, 4]
length = len(a)
print(length)

summation = sum(a)
print(summation)


# -

# #### **함수의 정의**
#   + 정의 시 최초에 def 키워드 사용
#   + argument 정의 (함수에 입력으로 전달하는 값을 의미, argument 또는 parameter라고 함) 
#   + : (콜론) -> 함수 역시 코드 블록이기 때문에 콜론(:) 필요
#   + body (함수의 구현 부분, 함수 역시 코드 블록이기 때문에 들여쓰기 된 부분까지 함수의 코드블록으로 인지 함)
#     - 함수를 호출한 코드 (caller)로 함수가 해당 기능을 수행하고 완료된 값(output)을 전달하기 위해 return 키워드 사용
#     - 즉, return 이후에 오는 값을 caller로 전달
#   + 함수의 네이밍 역시 중요
#     - 즉, 어떤 기능을 하는 함수인지 이름으로 최대한 나타날 수 있게 해야함
#     - e.g) get_a (x) get_student_name (o)

def add(x, y):
    n = x + y
    return n


# +
l = 3
c = add(30, 300)

print(c)
# -

# #### **함수의 사용(호출)**
#  + 함수명(파라미터1, 파라미터2, ... 파라미터n)
#  + 위와 같이 정의 된 함수의 이름과 전달되는 parameter(인자)를 괄호안에 전달하여 함수를 호출
#  + 함수가 호출되면 실행의 흐름이 호출자(caller)에서 함수(callee)로 변경 됨
#  
#  + 함수의 입력(인풋) 파라미터(parameter), 아규먼트(argument)라고도 함

c = add(30, 40)
print(c)


# #### **함수 네이밍(naming)**
#   * 함수 이름으로부터 기능이 명시 
#   * 의미와 반대되거나 맞지 않는 이름은 사용금지

# +
def substract(x, y):
    sub = x - y
    return sub

print(substract(4, 3))


# -

# #### **parameter(argument) (인자)**
#  + 함수에 전달되는 입력(input)
#  + 입력이 필요하지 않을 수도, 1개의 입력만 있을 수도, 여러개의 입력이 존재할 수 도 있음
#  + 파라미터로 int, string, float, boolm, list, dict 등등 어떤 파이썬 객체도 전달 가능
#  + 심지어, 함수도 함수의 파라미터로 전달 가능
#  
#  + python의 경우, 타입 명시가 없기 때문에, 함수 생성 시, 의도된 파라미터의 타입에 맞게 입력을 전달하는 것이 중요
#  + 또한 파라미터를 전달 할 때, 정의된 순서에 따라 값을 전달하는 것이 중요
#

# +
def substract(x, y):
    sub = x - y
    return sub

a = substract(100, 70)
print(a)


# -

# ####  Default parameter (기본 인자) 
#  + 함수의 파라미터에 기본값 지정 가능
#  + 파라미터를 명시하지 않을 경우, 지정된 기본값으로 대체

# +
def add(x, y=10, z=5):
    a = x + y + z
    return a

add(10, 1, 2)
# -

# * **기본 파라미터의 다른 예**
#  - print 함수
#    - sep, end, file등 여러 기본 파라미터를 가짐 

print(1, 2, 3, sep='!', end='%%%')
print(2, 3, 4, sep='p')


# ####  Default parameter 사용 시 주의 점
#   * 디폴트 파라미터 뒤에 일반 파라미터가 위치할 수 없음
#   
#   * e.g) 올바른 예
#     > def test(a, b, c = 1)
#     
#     > def test(a, b = 1, c = 2)
#     
#     > def test(a = 1, b = 1, c = 3)
#     
#   * e.g) 올바르지 않은 예
#     > def test(a, b = 1, c)
#     
#     > def test(a = 1, b, c)
#     
#     > def test(a = 1, b = 1, c)

# +
def test(a, b=3, c):
    print(a, b, c)
    
test(10, 20, 1)


# -

# #### **keyword parameter (키워드 파라미터)**
#   * 파이썬의 경우, 파라미터에 값을 전달 할 때, 파라미터의 이름을 명시하여 전달 가능
#   * 파라미터 이름을 사용하지 않을 경우, 기본적으로 순서에 맞게 전달

# +
def test(x, y, z):
    a = x + y + z
    return a

test(x=10, y=50, z=3)


# -

# #### **return (리턴)**
#  + 기본적으로 함수의 종료를 명시
#    + return 옆에 값이나 수식이 있다면 해당 값을 호출자(caller)에게 반환(전달)
#    + return 만 존재하면 None 반환
#    + return이 없는 경우, 기본적으로 함수 코드 블록이 종료되면 종료로 간주. 이때도 None 반환

# +
def weird_multiply(x, y):
    if x > 10:
        return x * y
    
    print(x + y)
    return (x + 2) * y

weird_multiply(12, 5)


# +
def weird_multiply(x, y):
    if x > 10:
        return x * y
    
    print(x + y)
    return (x + 2) * y

c = weird_multiply(12, 5)
print(c)


# +
def weird_multiply(x, y):
    if x > 10:
        return x * y
    
c = weird_multiply(2, 5)
print(c)


# -

# #### **multiple return (복수 값 반환)**
#  + tuple반환을 하여 복수개의 값 리턴 가능

# +
def add_mul(x, y):
    s = x + y
    m = x * y
    
    return s, m

a, b = add_mul(20, 3)
print(a, b)
# -

# #### **variable scope (변수의 범위)** 
#  + 변수가 참조 가능한 코드상의 범위를 명시
#  + 함수내의 변수는 자신이 속한 코드 블록이 종료되면 소멸됨
#  + 이렇게 특정 코드 블록에서 선언된 변수를 **지역변수(local variable)** 이라고 함
#  + 반대로 가장 상단에서 정의되어 프로그램 종료 전까지 유지되는 변수를 **전역변수(global variable)**이라고 함
#  + 같은 이름의 지역변수와 전역변수가 존재할 경우, 지역변수의 우선순위가 더 높음

print(num1, num2)

# +
num1 = 10
num2 = 30

def test(num1, num2):
    print(num1, num2)
    return num1 + num2

test(30, 40)
print(num1, num2)
    
# -

# #### **variable length argument (가변길이 인자)**
#  - 전달되는 파라미터의 개수가 고정적이지 않은 경우 사용
#  - e.g)
#    - print 함수
#    - format 함수
#   
# > ***args**,  ****kwargs**
#
# > ***args**    : 파라미터를 튜플의 형태로 전달
#
# > ****kwargs** : 파리미터를 딕셔너리 형태로 전달(네임드 파라미터)

# +
def test(*args): # arguments
    for item in args:
        print(item)
    
test(10, 30, 40, 50, 60, 70)
    
# -

# #### **keyword parameter (키워드 파라미터)**
#  - \**가 붙은 경우에는 키워드 파라미터로 인식
#  - 즉 함수 호출 시, 파리미터의 이름과 값을 함께 전달 가능

# +
def test2(**kwargs): # key word arguments 
    for key, value in kwargs.items():
        print('key:', key, ', value:', value)
    
test2(a=1)
    
# -

# * 가변길이 함수의 대표적인 예
#  **문자열 포맷 함수**
#  - 여러가지 값과 포맷을 이용하여 문자열을 정의할 수 있는 함수
#  - {} placeholder를 문자열 내에 위치 시킨 후, 해당 위치에 format함수로 전달된 값으로 대체하여 문자열 생성
#  - 포맷 구성은 다음 링크 참조 : https://pyformat.info/

a = '오늘 온도: {today_temp}도, 강수확률은: {today_prob}% 내일온도: {tomorrow_temp}도'.format(tomorrow_temp=23, today_prob=40, today_temp=40)
print(a)








