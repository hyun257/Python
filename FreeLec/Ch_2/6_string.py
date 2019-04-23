# -*- coding: utf-8 -*-
__author__ = 'hyun'

"""
자료형 :
Numbers/ String/ List/ Dictionaries/ Tuples/ Files
Slicing : [start:stop:step]
"""

s = 'Hello World'
print 's[:]'       , s[:]
print 's[0], s[2]' , s[0], s[2]
print 's[2:5]'     , s[2:5]
print 's[1:]'      , s[1:]
print 's[:9]'      , s[:9]
print 's[::2]'     , s[::2]
print 's[::-1]'    , s[::-1]    # 역순

# 문자열에 대한 직접 변경은 불가
# 따라서 슬라이싱과 연결하기를 이용
# ex.) s = 'h' + s[1:]

print len(s)

# string 변수에 특정 문자여리 있는지 확인
print 'World' in s