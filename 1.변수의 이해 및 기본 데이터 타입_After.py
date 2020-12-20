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
# 1. python 언어에서 변수의 의미 이해하기
# 2. 기본 데이터 타입 선언하기
#  - int, float, str, bool

# ### 기본 데이터 타입
# * variable declaration & value assignment (변수 선언 및 값 할당)

# ##### =  대입 연산자,  ==  비교 연산자 
#  - 대입의 경우, 오른쪽의 수식이나 값을 evaluation(여기서는 계산이라는 의미로 사용) 한 뒤, 
#  - 왼쪽에 명시된 변수에 해당 값을 대입
#  - 변수는 해당 값을 가지게 됨

a = 10 # int 
b = 11.4 # float 

# #### **comment(주석)**
#   - 코드에서 #으로 시작하는 뒷 부분은 실행되지 않음
#   - python이 소스코드를 실행하면서 #를 만나면 무시
#   - 개발자(사람)가 보기 위한 용도로 사용

# +
# this line is very important
# so don't delete those lines

a = 10
b = 11.4
# -

# #### **print 함수**
#   - 함수란 특정 기능을 반복적으로 호출하여 사용가능한 코드블럭
#   - 해당 변수의 값을 출력
#   - , 로 여러 변수를 나열하면 한줄에 출력
#   - 기본적으로는 한칸 띄어쓰기 후 출력

print(a, b)
print(a, 10, 200, b)

# * **print함수 설정**
#  - sep : 구분자, 각 출력할 변수 사이에서 구별하는 역할을 함
#  - end : 마지막에 출력할 문자열

print(a, b, 10, 100, sep='*', end='!!')

# #### **변수 값 확인법**
#  - print() 함수 사용
#  - 변수 값을 코드의 마지막에 위치 시킨 후 실행
#    - 이 경우 output으로 변수의 값이 출력

a = 10
b = 11.4
a
b

# #### **variable naming (변수 이름 규칙)**
#   - 숫자로 시작하는 이름을 제외하고 영문 대소문자, _, 숫자로 구성가능 
#   - 아래의 예제는 모두 valid한 변수 이름
#   - 일반적으로 해당 변수를 표현하고자 하는 정확하고 간결한 이름을 사용하는 것이 원칙
#     - 코드를 읽은 것을 더 쉽게 할 수 있음
#     - e.g) a = 1000의 경우보다 **student_num = 1000**로 명시한 것이 변수에 대한 이해가 빠름

# +
abcABC = 100
_abc124 = 200
ABC124 = 200
a456BC = 100

a = 200
number_of_students = 200
# -

# * **invalid한 변수 이름의 예**
#  - 숫자로 시작하면 안되는 이유는?

4 = 9

# #### **reserved keywords (예약어)**
#   - python에서 미리 선점하여 사용중인 키워드
#   - 변수, 함수, 클래스 등등의 사용자 정의 이름으로 사용할 수 없음

# +
for
while 
if
elif 
else 
class
try
except
class
# ...

_class = 100
print(_class)
# -

# ### 기본 데이터 타입 
#   - 정수 (int)
#   - 실수 (float)
#   - 문자열 (str)
#   - 불리언 (boolean)

# #### type 함수
#  - 해당 변수, 값의 타입(type)을 알고자 할 때 사용

# +
a = 10
b = 11.45

type(b)
# -

# #### **None**
#  - 아무런 값을 갖지 않을 때 사용
#  - 일반적으로 변수가 초기값을 갖지 않게 하여 해당 변수를 생성할 때 사용
#  - 기타 언어의 NULL, nil등과 같은 의미로 사용

c = None
print(c)

# #### **comparison operator(비교 연산자)** 
#   - 프로그래밍에서는 비교를 할 경우, = 대신 **==**를 사용
#   - <, > (작다, 크다)
#   - <=, >= (작거나 같다, 크거나 같다)
#   - == 같다
#   - != 같지 않다
#   - 비교 연산자의 결과는 bool 타입

# +
a = 5
b = 4

print(a > b) # True
print(a < b) # False
print(a >= b) # True
print(a <= b) # False
print(a == b) # False
print(a != b) # True

c = a > b
c = True
print(type(c))
print(c)
# -

# #### **numbers (숫자형 타입)**
#  - 정수, 실수로 구성
#  - 수학의 기본 연산자(가감승제) 사용 가능

# +
a = 5
b = 4

print(a + b)
print(a * b)
print(a - b)
print(a / b)
print(a % b)
print(a ** b)

# -

# #### **operator priorities (연산자 우선순위)**
#   - 기본적인 수학의 연산자와 동일
#   - 강제로 연산을 선수하기 위해선, 괄호()를 사용

# +
a = 5
b = 4

print(a + b * 4)
print((a + b) * 4)
# -

# *  **연습문제** 다음의 각 a값을 출력 했을 때 결과는? 
#

a = 9
print(a) # 9
print(a - 3) # 6
print(a) #9, 6

# #### **expression evaluation & assignment (식평가 & 대입)**
#  - 변수의 값이 변경되기 위해서는 =를 사용하여 대입이 발생하는 경우에만 해당

a = 9
a-3
print(a)

# +
a = 9
t = a - 3
a = t

print(a)
# -

a = 9
a = a - 3
print(a)

a = 9
# a = a - 3
a **= 3
print(a)






