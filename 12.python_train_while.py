#while 조건을 만족할때까지 반복

# customer="토르"
# inex=5d
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다.{1}번 남았어요.".format(customer,index))
#     index -=1  #1번씩 줄여나감
#     if  index ==0:  #index가 0이되었을때
#         print("커피는 폐기처분되었습니다.")


# customer2="아이언맨"
# index2=1
# while True: 
#     print("{0}, 커피가 준비되었습니다.호출 {1}회".format(customer2,index2))
#     index2 +=1  #index에 1씩 더함 
#     #무한루프 종료:ctrl +c

customer="토르"
person ="Unknown"

while person != customer:  #person이 내가 원하는 손님이 아닐때 반복
    print("{0}, 커피가 준비되었습니다.".format(customer,person))
    person = input("이름이 어떻게 되세요?")
