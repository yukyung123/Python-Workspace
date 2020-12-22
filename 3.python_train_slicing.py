#####슬라이싱

jumin="990120-1234567"

print("성별:"+jumin[7])
print("연:"+jumin[0:2])  #0부터 2직전까지
print("월:"+jumin[2:4])
print("일:"+jumin[4:6])
print("생년월일:" + jumin[:6])
print("뒤 7자리"+ jumin[7:])
print("뒤 7자리(뒤에서부터)"+ jumin[-7:])  #맨뒤 7부터 끝까지

#문자열 처리 함수
python="Python is Amazing"
print(python.lower())  #python값을 소문자로 출력
print(python.upper())  #python값을 대문자로 출력
print(python[0].isupper())  #python[0]에 있는값이 대문자인가?
print(len(python))  #python의 글자수 출력\
print(python.replace("Python","Java"))

index = python.index("n")  #python에서 n의 위치 
print(index)
index=python.index("n", index +1)  # python에서 두번째 n의 위치
print(index)
print(python.find("n"))  #python에서 n의 위치 
print(python.find("Java"))  #python에서 n의 위치 결과=-1
#print(python.index("Java"))  #python에서 n의 위치결과=error,이후 프로그램이 진행되지 않음

print(python.count("n"))#python에서 n의 개수 

####문자열 포맷
print("a"+"b")
#방법1
print("나는 %d살입니다."%20) #(d는 정수) 20살 출력 
print("나는 %s를 좋아해요"%"파이썬")  #(s는 문자열 string값) 파이썬 출력
print("apple은 %c로 시작해요"%"a")#(c는 한글자,문자) a출력
#%s로 다 가능

print("나는 %s색과 %s색을 좋아해요." %("파란","빨간"))  #동시출력

#방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))  #동시출력
print("나는 {1}색과 {0}색을 좋아해요." .format("파란","빨간"))  #중괄호 안에 숫자를 넣어 순서를 바꿀 수도 있음

#방법3
print("나는 {age}살이며,{color}색을 좋아해요".format(age=20,color="빨간"))

#방법4 (v3.6이상)
age=20
color="빨간"
print("나는 {age}살이며,{color}색을 좋아해요.") #왜 나는 안될까^^

####탈출문자
 #\n줄바꿈
print("백문이 불여일견\n백견이 불여일타") 


#\" \':문장내 따옴표
#예제:저는 "김유경"입니다.
print("저는 '김유경'입니다.")
print('저는 "김유경"입니다.')
print("저는 \"김유경\"입니다.")

#\\:문장내에서 \
print("PS C:\\Users\\USER\\Desktop\\Python Workspace> ")

#\r 커서를 맨앞으로 이동
print("red Apple \r pine")

#\b 백스페이스(한글자 삭제)
print("redd\bapple")

#\t 탭
print("red\tapple")

#Quiz 사이트별로 비밀번호를 만들어주는 프로그램 작성 
#예)http://naver.com 
#규칙1:http://부분 제외 =>naver.com
#규칙2:처음만나는 점(.)이후 부분은 제외 =>naver
#규칙3:남은글자중 처음 세자리 +글자갯수 +글자내 'e'갯수 +"!"로 구성 
#예)생성된 비밀번호: nav51!

pw="http://naver.com"

print(pw[7:])
print(pw[7:12])
pw3=pw[7:10]+str(len(pw))+str(pw.count("e"))+"!"
print(pw3)


p1=pw.replace("http://","")
print(p1)
p2=p1[:p1.index(".")]#p1[0:5]->0~5직전까지.
print(p2)
p3= pw[7:10]+ str(len(p2)) + str(pw.count("e"))+"!"
print("{}의 비밀번호는 {}입니다.".format("naver",p3))