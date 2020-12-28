#지역변수와 전역변수 
gun= 10

def checkpoint(soldiers):
    gun=20
    gun= gun-soldiers  #함수 내 만들어진 총(지역변수)
    print("[함수 내] 남은 총:{}".format(gun))
#답 18

print("전체 총: {}".format(gun))
checkpoint(2)
print("남은 총 : {}".format(gun))

def checkpoint(soldiers):
    global gun #전역공간에 있는 gun 사용  10사용될것임
    gun= gun-soldiers  #함수 내 만들어진 총(지역변수)
    print("[함수 내] 남은 총:{}".format(gun))
#답 8

print("전체 총: {}".format(gun))
checkpoint(2)
print("남은 총 : {}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun= gun -soldiers #지역변수
    print("[함수 내] 남은 총:{}".format(gun))
    return gun

gun=checkpoint_ret(gun, 2)
print("남은 총: {}".format(gun))