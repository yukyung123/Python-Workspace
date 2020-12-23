

# #내답
# person = range(1,51)
# time =randint(range(5,16),1)
#  for person in range(1,51)
#      print("[0] {1}번째 손님(소요시간:{1}분)".format(person,time))
#  if  16<=time<50:
#  print("[ ] {1}번째 손님(소요시간:{1}분)".format(person,time)))

from random import*
cnt=0 #총 탑승 승객

for i in range(1,51):
    time=randrange(5,51) #5-50분 소요시간 
    if 5<=time<=15: #5~10분 이내의 손님, 탑승 승객수 증가처리
        print("[0] {0}번째 손님(소요시간 {1}분".format(i,time))
        cnt +=1 #1씩 증가처리 
    else:
        print("[ ] {0}번째 손님(소요시간 {1}분".format(i,time))
print("총 탑승 승객: {0}분".format(cnt))


     
