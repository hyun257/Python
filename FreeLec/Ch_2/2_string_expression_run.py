# -*- coding: utf-8 -*-
__author__ = 'hyun'

# eval() : 단순식
a = 1
a = eval('a + 4')
print 'a =', a

b = 0
b = eval('a * 5')
print 'b =', b

# exec() : 등식
c = 0
exec_script = \
'''
c = a + b + c; print 'c =', c
'''

exec(exec_script)

# comfile() : http://blog.naver.com/bbh1988?Redirect=Log&logNo=40209364020
# comfile() : 하나의 문
code = compile("print 'a + 1 = ', a + 1", '<string>', 'single')
exec code
print

# comfile() : 파일 실행시키기
fileopen   = open('3_compile_test_file.py').read()
script_run = compile(fileopen, '3_compile_test_file.py', 'exec')
exec(script_run)

# exec : 스크립트 안에서 파일 실행시키기
# exec open('3_compile_test_file.py')

