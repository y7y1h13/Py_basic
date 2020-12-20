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
#  * 조건문의 이해 및 활용 (if)

# #### condition (조건문)
#  + 특정 조건을 만족하는 경우에만 수행할 작업이 있는 경우 사용
#  + 모든 조건은 boolean으로 표현 됨 (예외 사항은 아래 배울 예정)
#  + if, elif, else 키워드가 사용
#  + 조건문의 경우 if, elif, else 블록에 종속된 코드는 들여쓰기로 표현 가능
#  + 즉 아래코드에서와 같이, 조건문 아래에 들여쓰기된 2줄의 코드만이 조건문의 조건에 따라 수행될 수도, 수행되지 않을 수도 있는 코드라고 할 수 있음
#  + 들여쓰기 된 코드를 블록(block), 또는 코드블록이라고 함
#  + python에서 모든 블록의 시작점의 마지막에는 :(콜론, colon) 추가가 필요
#
# ```python
# if 6 >= 5:
#     print ('6 is greater than 5')
#     print ('Yeah, it is true')
# print ('This code is not belongs to if statements')
# ```

# +
if 6 >= 5:
    print('6 is greater than 5')
    print('Yeah, it is true')
    print('it is really true')
    
print ('This code is not belongs to if statements')

# +
if 6 == 5:
    print('6 is greater than 5')
    print('Yeah, it is true')
    print('it is really true')
    
print ('This code is not belongs to if statements')
# -

# * Logical AND, OR, NOT 
#   - 조건문에 사용되는 조건의 경우, boolean이기 때문에, 논리식 AND, OR, NOT 이 사용가능
#   - AND : and
#   - OR : or
#   - NOT : not
#   
# * 논리표 
#   - AND 
#       - T AND T : T
#       - T AND F : F
#       - F AND T : F
#       - F AND F : F
#   - OR 
#       - T OR T : T
#       - T OR F : T
#       - F OR T : T
#       - F OR F : F
#       
#   - NOT 
#       - NOT T : F
#       - NOT F : T
# * 우선순위
#   - NOT > AND > OR

a = 10
b = 8
c = 11

if (a == 10 or b == 9) and c == 12:
    print('that is true')

if not a == 10:
    print('a is ten')

# #### if의 조건이 bool이 아닌 경우
#  * 일반적으로는 조건문에는 bool이 주로 위치 함
#  * 하지만, 정수, 실수, 문자열 리스트 등 기본 타입도 조건에 사용 가능
#  * False로 간주되는 값 (각 타입의 기본값)
#      * None
#      * 0
#      * 0.0
#      * ''
#      * [] -> 빈 리스트
#      * () -> 빈 튜플
#      * {} -> 빈 딕셔너리
#      * set() -> 빈 집합
#  * 그밖에는 모두 True로 간주

a = []
if a:
    print('print')

# #### if, else
#   - if가 아닌 경우, 나머지 조건을 표현하고 싶다면 바로 아래 else 블락 사용
#   - 이 경우, if조건이 True인 경우, if 블락의 코드가 수행, 거짓인 경우 else 블락의 코드가 수행
#   - 주의 할 점 : if와 else사이에 다른 코드 삽입 불가

# +
# 짝수인 경우에는 2로 나눈 값을 출력하고
# 홀수인 경우에는 1을 더한 값을 출력해라

a = 12
if a % 2 == 0: # 짝수인지 판별
    print(a / 2)
else:
    print(a + 1)
# -

# #### if, elif, else
#   - 조건이 여러개인 경우, 다음 조건을 elif 블록에 명시 가능
#   - 이 경우, 각 조건을 확인 후, True인 조건의 코드 블락을 실행 한 후, 전체 if, elif, else 구문을 종료
#   - 조건문을 사용할 때는, if 이후, 0개 이상의 elif를 사용 가능하며 0개 또는 1개의 else를 사용 가능함
#
# ```python
# a = 17
# if a % 4 == 0:
#     print 'a is divisible by 4'
# elif a % 4 == 1:
#     print 'a % 4 is 1'
# elif a % 4 == 2:
#     print 'a % 4 is 2'
# else:
#     print 'a % 4 is 3'
# ```

# +
a = 16
if a % 4 == 0:
    print('a is divisible by 4')
elif a % 4 == 1:
    print('a % 4 is 1')
elif a % 4 == 2:
    print('a % 4 is 2')
else:
    print('a % 4 is 3')
    


# -

a = 16
if a % 4 == 0:
    print('a is divisible by 4')
if a % 4 == 1:
    print('a % 4 is 1')
if a % 4 == 2:
    print('a % 4 is 2')
else:
    print('a % 4 is 3')

# #### 중첩 조건문(nested condition)
#   - 조건문의 경우 중첩하여 작성 가능
#   - 중첩의 의미는 depth(깊이)로 생각할 수 있으며, depth의 제한은 없음

# +
a = 10
b = 9
c = 8

if a == 10:
    if c == 8:
        if b == 8:
            print('a is ten and b is 8')
        else:
            print('a is ten and b is not 8')
