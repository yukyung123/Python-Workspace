#숫자형 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

#문자형 자료형
print('풍선')
print("나비")
print("ㅋ"*9)

#분리안
print(5>10)
print(5<10)
print(True)
print(not True)
print(not (5>10))
#변수 애완동물을 소개해주세요

name="감자"
animal="고양이"
age=4
hobby="산책"
is_adult = age >= 3


print("우리집" + animal + " 의 이름은 " + name + "에요")
hobby="낮잠"
print( name, "는" , age , "살이며," + hobby + "을 아주좋아해요")
print("감자는 어른일까요? "+str(is_adult))
'''이렇게하면
여러문장이
주석처리 됩니다'''

#(quiz)
station="사당"

print(station,"행 열차가 들어오고 있습니다.")

#연산자
print(1+1)
print(6/3)

print(2**3)#2^3
print(5%3)#나머지
print(5//3)#몫

print(10>3)
print(4>=7)

print(3==3)#앞과 뒤가 똑같은지
print(3+4==7)

print(1!=3) #앞뒤가 같지 않다.
print(not(1!=3))
print((3>0)and (3<5))
print((3>0)&(3<5))

print((3>0)or (3>5))
print((3>0)| (3>5))
print(5>4>3)