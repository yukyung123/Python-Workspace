print("python","java", sep=",") #단어간 연결 모양

print("python","java", end="?") #뒷문장이 연달아 한문장으로 출현 
print("무엇이 더 재밌을까요?") 


import sys
print("python","java", file=sys.stdout)#표준출력
print("python","java", file=sys.stderr)#표준에러로 출력

scores = {"수학":0 ,"영어":50,"코딩":100 }
for subject, score in scores.items(): #items: key와 value 코어로 나옴/tuple
    #print(subject,score)
    print(subject.ljust(8),str(score).rjust(4),sep=":") #총 8칸의 공간을 확보한 상태에서 왼쪽정렬
    
    
#은행 대기 순번표

#001,002,003,,,,
for num in range(1,21):
    print("대기번호:"+str(num).zfill(3)) #0채우기


answer = input("아무값이나 입력하세요:")
print("입력하신 값은" + answer+ "입니다.")
#사용자 형태로 지정받은 값은 항상 문자열(str)