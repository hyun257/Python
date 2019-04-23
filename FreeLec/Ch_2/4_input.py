# -*- coding: utf-8 -*-
__author__ = 'hyun'


import random

# name = raw_input('type your name :')
# print 'your name is :', name

# 스무고개 게임
print("스무고개 게임을 시작합니다.")
print('1 에서 100 까지의 숫자 중 하나를 마음속에 정하세요.')
print("")

max_val = 100
min_val = 1
temp    = max_val/2
count   = 0

while count <= 20:

    response = raw_input('당신이 생각한 숫자가 %d입니까? (y/n 로 대답하세요)' % temp)
    count += 1
    if response.lower() == 'y':
        print("당신이 생각하신 숫자는 %d, %d번에 정답을 맞췄습니다!") % (temp, count)
        break
    elif response.lower() == 'n':
        print("아니라고? 그럼 더 고민을... 흠")
        print

    response = raw_input('당신이 생각한 숫자가 %d보다 큽니까? (y/n 로 대답하세요)' % temp)
    count += 1
    if response.lower() == 'y':
        min_val = temp + 1
        if min_val > max_val:
            print("거짓말치네 칵!")
            break
        elif min_val == max_val:
            print("당신이 생각하신 숫자는 %d, %d번에 정답을 맞췄습니다!") % (min_val, count)
            break
        else:
            temp = random.randrange(min_val, max_val)

    elif response.lower() == 'n':
        max_val = temp - 1
        if min_val > max_val:
            print("거짓말치네 칵!")
            break
        elif max_val == min_val:
            print("당신이 생각하신 숫자는 %d, %d번에 정답을 맞췄습니다!") % (max_val, count)
            break
        else:
            temp = random.randrange(min_val, max_val)

if count == 20:
    print("아이고 못 맞췄네. ㅠㅠ")
