#사전 단어;뜻 key;value

cabinet={3:"유재석",100:"김태호"}
print(cabinet[3])  #유재석
print(cabinet[100])  #김태호 

print(cabinet.get(3))
print(cabinet.get(5))#print(cabinet[5])는 에러
print(cabinet.get(5,"사용가능" ))  # 5값이 없다면 "사용가능"표시

#사전안에 어떤 자료가 있는지 확인
print(3 in cabinet)  #true
print(5 in cabinet)  #false


#정수가 아닌 string도 가능
cabinet={"a-3":"유재석","b--100":"김태호"}
print(cabinet["a-3"])

#새손님
cabinet["a-3"]="김종국"  #기존값 수정가능 
cabinet["c-20"]="조세호"  #값 추가 가능
print(cabinet)

#간 손님
del cabinet["a-3"]
print(cabinet)

#key들만 출력 
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)