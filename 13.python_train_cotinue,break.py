
#continue:뒤 문장을 실행하지 않고 다음 반복으로 넘어감  
#break: 반복문 탈출 
no_book=[7] #책을 깜빡함
absent=[2,3] #결석 ,결석자는 책을 읽을 수 없음 
for student in range(1,11):
    if student in absent:
        continue  
    elif student in no_book:
        print("오늘 수업 여기까지.{0}는 교무실로 따라와".format(student))
        break  
    print("{0},책을 읽어봐",format(student))
