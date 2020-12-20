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
#  1. module의 이해 및 module import 하기

# ### **모듈 임포트**
#  + 그동안 사용했던 함수들 처럼, 다양한 기능들이 미리 함수로 구현되어 모듈 형태로 제공
#  + 대표적으로 추후 과정에서 사용하게 될 아래의 모듈들이 존재
#
#  + requests - HTTP 요청/응답 모듈
#  + numpy - 수치해석 모듈 
#  + pandas - 데이터 분석 모듈
#

import requests
resp = requests.get('http://naver.com')
resp.text



# #### import 
#  - import를 사용하여 해당 모듈 전체를 import

import math

math.pi

math.cos(100)

# #### from import 
#  - 해당 모듈에서 특정한 타입만 import

from math import pi
from math import cos
#from math import sin

cos(100)

# #### \* 임포트
#  - 해당 모듈내에 정의된 모든 것을 import
#  - 일반적으로 사용이 권장되지 않음

from math import cos

# #### as 
#  - 모듈 import 시, alias(별명) 지정가능
#  

import math as m
m.exp(3)
m.cos(100)
