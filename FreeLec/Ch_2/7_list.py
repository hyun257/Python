# -*- coding: utf-8 -*-
__author__ = 'hyun'

# index  : 값의 index 를 반환
# count  : 값의 개수를 반환
# append : 해당값을 List의 마지막 element로 추가
L = [1, 2, 3, 4]
L.append(5)
print 'index :',    L.index(2)
print 'count :',    L.count(2)
print 'append 5 :', L

# insert : 입력된 index 순서에 입력된 value를 추가
L = [1, 2, 3, 4]
L.insert(2, 2.5)
print 'insert 2.5 :', L

# remove : 가장 최초로 나오는 값을 삭제
L = [1, 2, 3, 4]
L.remove(2)
print 'remove :', L

# pop : 입력값을 지정해주지 않으면 마지막 값을 return 하고 본래 List에서는 마지막 element가 제거됨
#       입력값(index)를 입력하면 입력된 index에 해당하는 값을 return 하고 본래 List에서는 index에 해당하는 element가 제거됨
L = [1, 2, 3, 4]
print 'L.pop() :', L.pop()
print 'L.pop() 이후 L:', L
L = [1, 2, 3, 4]
print 'L.pop(2) :', L.pop(2)
print 'L.pop(2) 이후 L :', L

# sort    : 정렬
L = [1, 4, 2, 3]
L.sort()
print 'sort :'   , L

# reverse : 원래 List를 역방향으로 뒤집어 줌(역순정렬이 아님)
L = [1, 4, 2, 3]
L.reverse()
print 'reverse :', L

# del : 입력 index에 해당하는 값을 삭제x
L = [1, 4, 3, 2]
del L[2]
print 'del :', L

