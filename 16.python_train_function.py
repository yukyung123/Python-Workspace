#함수 =box
def open_account():
    print("새로운 계좌가 생성되었습니다")

open_account()

def deposit(balance,money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다".format(balance+money))
    return balance+money

def withdraw(balance, money):
    if balance >= money:  #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance- money
    else:
        print("출금이 완료되지 않았습니다. 잔액은{0}원입니다".format(balance))
        return balance

def withdraw_nigtht(balance,money):
    commission=100
    return commission, balance-money-commission

balance=0
balance =deposit(balance,1000)
print(balance)

balance = withdraw(balance,2000)
print(balance)
balance = withdraw(balance,500)
print(balance)
commission,balance = withdraw_nigtht(balance,500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))