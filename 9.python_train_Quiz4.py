#Quiz4)나도코딩(기본편) 1:51:00
from random import *

#나의답
# lst=[1,2,3,4,5] 
# print(lst)
# shuffle(lst)

# ch=sample(lst,1)
# co=lst.remove(ch)
# co=sample(co,3)
# print(ch)
# print(co)
# print("--당첨자발표--\n 치킨당첨자 : {ch}\n커피 당첨자 :{co}\n--축하합니다--")

users=range(1,21)#1부터 20까지 생성
users=list(users)
print(type(users))

shuffle(users)
print(users)

winners = sample(users,4)
print("--당첨자발표--")
print("치킨 당첨자:{0}".format(winners[0]))
print("커피 당첨자:{0}:".format(winners[1:4]))
print("--축하합니다--")