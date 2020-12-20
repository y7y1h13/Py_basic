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
#  1. 클래스와 오브젝트에 대한 이해

# #### **class란?**
#  + 실세계의 것을 모델링하여 속성(attribute)와 동작(method)를 갖는 데이터 타입
#  + python에서의 string, int, list, dict.. 모두가 다 클래스로 존재
#  + 예를들어 학생이라는 클래스를 만든다면, 학생을 나타내는 속성과 학생이 행하는 행동을 함께 정의 할 수 있음
#  + 따라서, 다루고자 하는 데이터(변수) 와 데이터를 다루는 연산(함수)를 하나로 캡슐화(encapsulation)하여 클래스로 표현
#  + 모델링에서 중요시 하는 속성에 따라 클래스의 속성과 행동이 각각 달라짐

a = [1, 2, 3, 4]
a.append(5)
print(a)

# #### **object 란?**
#  - 클래스로 생성되어 구체화된 객체(인스턴스)
#  - 파이썬의 모든 것(int, str, list..etc)은 객체(인스턴스)
#  - 실제로 class가 인스턴스화 되어 메모리에 상주하는 상태를 의미
#  - class가 빵틀이라면, object는 실제로 빵틀로 찍어낸 빵이라고 비유 가능
#



# #### **class 선언하기**
#   - 객체를 생성하기 위해선 객체의 모체가 되는 class를 미리 선언해야 함 

class Person:
    pass


# +
bob = Person()
cathy = Person()

a = list()
b = list()

print(type(bob), type(cathy))
print(type(a), type(b))


# -

# #### \_\_init__(self)
#  + 생성자, 클래스 인스턴스가 생성될 때 호출됨
#  + self인자는 항상 첫번째에 오며 자기 자신을 가리킴
#  + 이름이 꼭 self일 필요는 없지만, 관례적으로 self로 사용
#  
#  + 생성자에서는 해당 클래스가 다루는 데이터를 정의
#    - 이 데이터를 멤버 변수(member variable) 또는 속성(attribute)라고 함

# +
class Person:
    def __init__(self):
        print(self, 'is generated')
        self.name = 'Kate'
        self.age = 10
        
p1 = Person()
p2 = Person()

p1.name = 'aaron'
p1.age = 20

print(p1.name, p1.age)


# +
class Person:
    def __init__(self, name, age=10):
        # print(self, 'is generated')
        self.name = name
        self.age = age
        
p1 = Person('Bob', 30)
p2 = Person('Kate', 20)
p3 = Person('Aaron')

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)


# -

# #### **self**
#  - 파이썬의 method는 항상 첫번째 인자로 self를 전달
#  - self는 현재 해당 메쏘드가 호출되는 객체 자신을 가리킴
#  - C++/C#, Java의 this에 해당
#  - 역시, 이름이 self일 필요는 없으나, 위치는 항상 맨 처음의 parameter이며 관례적으로 self로 사용

# +
class Person:
    def __init__(self, name, age):
        print('self: ', self)
        self.name = name
        self.age = age
        
    def sleep(self):
        print('self:', self)
        print(self.name, '은 잠을 잡니다.')
        
a = Person('Aaron', 20)
b = Person('Bob', 30)

print(a)
print(b)

a.sleep()
b.sleep()

# -



# #### **mehtod 정의**
#  + 멤버함수라고도 하며, 해당 클래스의 object에서만 호출가능
#  + 메쏘드는 객체 레벨에서 호출되며, 해당 객체의 속성에 대한 연산을 행함
#  + {obj}.{method}() 형태로 호출됨

# +
# 1. 숫자를 하나 증가
# 2. 숫자를 0으로 초기화
class Counter:
    def __init__(self):
        self.num = 0
        
    def increment(self):
        self.num += 1
    
    def reset(self):
        self.num = 0
        
    def print_current_value(self):
        print('현재값은:', self.num)
        
    
c1 = Counter()
c1.print_current_value()
c1.increment()
c1.increment()
c1.increment()
c1.print_current_value()

c1.reset()

c1.print_current_value()

c2 = Counter()
c2.increment()
c2.print_current_value()


# -

# #### **method type**
#  - instance method - 객체로 호출
#    - 메쏘드는 객체 레벨로 호출 되기 때문에, 해당 메쏘드를 호출한 객체에만 영향을 미침
#  - class method(static method) - class로 호출
#    - 클래스 메쏘드의 경우, 클래스 레벨로 호출되기 때문에, 클래스 멤버 변수만 변경 가능
#

# +
class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
Math.add(10, 20)
Math.multiply(10, 20)


# -

#  #### **Class Inheritance (상속)**
#   - 기존에 정의해둔 클래스의 기능을 그대로 물려받을 수 있다.
#   - 기존 클래스에 기능 일부를 추가하거나, 변경하여 새로운 클래스를 정의한다.
#   - 코드를 재사용할 수 있게된다.
#   - 상속 받고자 하는 대상인 기존 클래스는 (Parent, Super, Base class 라고 부른다.)
#   - 상속 받는 새로운 클래스는(Child, Sub, Derived class 라고 부른다.)
#   - 의미적으로 is-a관계를 갖는다

# +
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self, food):
        print('{}은 {}를 먹습니다.'.format(self.name, food))
    
    def sleep(self, minute):
        print('{}은 {}분동안 잡니다.'.format(self.name, minute))
    
    def work(self, minute):
        print('{}은 {}분동안 일합니다.'.format(self.name, minute))

class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Employee(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

bob = Employee('Bob', 25)
bob.eat('BBQ')
bob.sleep(30)
bob.work(60)
    
    
# -

# #### **method override**
#  - 부모 클래스의 method를 재정의(override)
#  - 하위 클래스(자식 클래스) 의 인스턴스로 호출시, 재정의된 메소드가 호출됨

# +
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self, food):
        print('{}은 {}를 먹습니다.'.format(self.name, food))
    
    def sleep(self, minute):
        print('{}은 {}분동안 잡니다.'.format(self.name, minute))
    
    def work(self, minute):
        print('{}은 {}분동안 일합니다.'.format(self.name, minute))

class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self, minute):
        print('{}은 {}분동안 공부합니다.'.format(self.name, minute))
        
class Employee(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self, minute):
        print('{}은 {}분동안 업무를 합니다.'.format(self.name, minute))
        
bob = Employee('Bob', 25)
bob.eat('BBQ')
bob.sleep(30)
bob.work(60)


# -

# #### super 
#  - 하위클래스(자식 클래스)에서 부모클래스의 method를 호출할 때 사용

# +
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self, food):
        print('{}은 {}를 먹습니다.'.format(self.name, food))
    
    def sleep(self, minute):
        print('{}은 {}분동안 잡니다.'.format(self.name, minute))
    
    def work(self, minute):
        print('{}은 {}분동안 준비를 합니다.'.format(self.name, minute))

class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self, minute):
        super().work(minute)
        print('{}은 {}분동안 공부합니다.'.format(self.name, minute))
        
class Employee(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self, minute):
        super().work(minute)
        print('{}은 {}분동안 업무를 합니다.'.format(self.name, minute))
        
bob = Employee('Bob', 25)
bob.eat('BBQ')
bob.sleep(30)
bob.work(60)


# -

# #### **special method**
#  - __로 시작 __로 끝나는 특수 함수
#  - 해당 메쏘드들을 구현하면, 커스텀 객체에 여러가지 파이썬 내장 함수나 연산자를 적용 가능
#  - 오버라이딩 가능한 함수 목록은 아래 링크에서 참조 
#    - https://docs.python.org/3/reference/datamodel.html
#    - https://docs.python.org/3/reference/datamodel.html#object.__add__

# +
# Point 
# 2차원 좌표평면 각 점(x, y) 
# 연산
# 두점 의 덧셈, 뺄셈 (1, 2) + (3, 4) = (4, 6)
# 한점과 숫자의 곱셈 (1,  2) * 3 = (3, 6)
# 그 점의 길이 (0,0) 부터의 거리
# x, y 값 가져오기
# 출력하기

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        
    def __add__(self, pt):
        new_x = self.x + pt.x
        new_y = self.y + pt.y
        return Point(new_x, new_y)
    
    def __sub__(self, pt):
        new_x = self.x - pt.x
        new_y = self.y - pt.y
        return Point(new_x, new_y)
    
    def __mul__(self, factor):
        return Point(self.x * factor, self.y * factor)
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            return -1
    
    def __len__(self):
        return self.x ** 2 + self.y ** 2
        
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
        
p1 = Point(3, 4)
p2 = Point(2, 7)

a = 1 + 2
p3 = p1 + p2
p4 = p1 - p2

# p5 = p1.multiply(3)
p5 = p1 * 3

print(len(p1))

# p1[0] -> x
# p1[1] -> y
print(p1[0])
print(p1[1])
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
# -

# #### 연습문제)
#  - 복소수 클래스를 정의 해봅시다.
#  - 덧셈, 뺄셈, 곱셈 연산자 지원
#  - 길이 (복소수의 크기) 지원 
#  - 복소수 출력 '1 + 4j'와 같이 표현
#  - 비교 연산 ==, != 지원
#  - >=, <= , <, > 연산 지원
#  - 절대값 지원
#

# +
import math
class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def __add__(self, cn):
        return ComplexNumber(self.real + cn.real, self.img + cn.img)
    
    def __sub__(self, cn):
        return ComplexNumber(self.real - cn.real, self.img - cn.img)
    
    def __mul__(self, x):
        if type(x) == int:
            return ComplexNumber(self.real * x, self.img * x)
        elif type(x) == ComplexNumber:
            return ComplexNumber(self.real * x.real - self.img * x.img, self.real * x.img + self.img * x.real)
#            (a + bj) * (c + dj) = (ac - bd) + (ad + bc)j
        
    def __str__(self):
        if self.img >= 0:
            return '{} + {}j'.format(self.real, self.img)
        else:
            return '{} - {}j'.format(self.real, abs(self.img))
        
    def __eq__(self, cn):
        return self.real == cn.real and self.img == cn.img
    
    def __ne__(self, cn):
        return not (self.real == cn.real and self.img == cn.img)
    
    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.img ** 2)
    
    def __len__(self):
        return self.real ** 2 + self.img ** 2
    
a = ComplexNumber(1, 2)
b = ComplexNumber(3, 2)

abs(a)
len(a)
# -


