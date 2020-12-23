#for list 내 값을 순서대로 작업 수행 

print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")

for waiting_no in range(0,4):  #range(5)=[0,1,2,3,4]
    print("대기번호 :{0}".format(waiting_no)) # list 내 값을 순서대로 작업 수행 

starbucks=["아이언맨", "토르","그루트"]
for customer in starbucks:
    print("{0},커피가 준비되었습니다",format(customer))