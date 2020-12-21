print(2+3*4)

number=2+3*4

print(number)

number = number+2
print(number)
number+=2
print(number)
number*=2
print(number)


print(abs(-5))
print(pow(4,2))#4^2= 4^4
print(round(3.14))#반올림 

from random import *
print(random())#0이상 1미만의 임의의 값 생성
print(random()*10)#0이상 10미만
print(int(random()*10)) 
print(random()*10+1)

print(int(random()*45+1))
print(randrange(1,46))

#(quiz)
from random import *
print(randint(4,28))
print(randint(4,28))
print(randint(4,28))
print()

date= randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 "+str(date)+"일로 선정되었습니다.")

sentence="나는 소년입니다."
print(sentence)
sentence2='파이썬은 쉬워요'
print(sentence2)
sentence3="""
나는 소년이고 파이썬은
쉬워요
"""
print(sentence3)
