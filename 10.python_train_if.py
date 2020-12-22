# if 조건:
#     실행명령문


weather="맑아요"
if weather =="비":
    print("우산을 챙기세요")    
elif weather =="미세먼지":
    print("마스크를 챙기세요")  #if 문장 추가
else:
    print("준비물 필요 없어요 ")  #if 가 아닐경우 else출현



weather2=input("오늘 날씨는 어때요? ")#input 질문
if weather2 =="비" or weather2 == "눈": #같은 답안 if문장 추가 
    print("우산을 챙기세요")    
elif weather2 =="미세먼지":
    print("마스크를 챙기세요")  
else:
    print("준비물 필요 없어요 ") 



temp = int(input("기온은 어때요?"))
if 30<= temp:
    print("너무 더워요 나가지 마세요")
elif 10<= temp and temp <30:
    print("괜찮은 날씨에요")
elif 0<= temp <10:
    print("외투를 챙기세요 ")
else: 
    print("너무 추워요 나가지 마세요 ")