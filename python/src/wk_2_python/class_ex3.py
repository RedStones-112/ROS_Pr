import random 
class Account:
    account_num = 0
    account_num_list = []
    def __init__(self,name, money):
        self.name = name
        self.money = money
        self.deposit_count = 0
        Account.account_num +=1

        while 1:
            rand_number = str(round(random.random() * (10 **13)))
            if Account.account_num_list.count(f"크크크은행 {rand_number[0:4]}-{rand_number[4:6]}-{rand_number[6:]}") != 0 or 13 != len(rand_number):
                print("잘못된 계좌번호입니다. 재생성합니다.")
                continue
            else:
                Account.account_num_list.append(f"크크크은행 {rand_number[0:4]}-{rand_number[4:6]}-{rand_number[6:]}")
                self.account_nums = f"크크크은행 {rand_number[0:4]}-{rand_number[4:6]}-{rand_number[6:]}"
                break
        
        
    def get_account(self):
        print(self.account_num)
    def deposit(self,in_money):
        if in_money >= 1:
            self.money+=in_money
            print(f"입금액 : {in_money}")
            self.deposit_count += 1
        else:
            print("입금은 1원 이상부터 가능합니다.")

        if self.deposit_count%3 == 0:
            self.money = round(self.money*1.03)
        print(f"잔액 : {self.money}")
        
    def withdraw(self, out_money):
        if self.money < out_money:
            print("잔액이 부족합니다.")
        else:
            self.money-=out_money
            print(f"출금액 : {out_money}")
        print(f"잔액 : {self.money}")

        
    def print_info(self):###
        print(f"name : {self.name}")
        print(f"""money : {format(self.money,",")} """)
        print(f"deposit_count : {self.deposit_count}")
        
def main():
    A1 = Account("lili",20)
    A2 = Account("nono", 30)
    A3 = Account("mama", 5000)
    A1.get_account()
    A1.deposit(3000)
    A1.deposit(3000)
    A1.deposit(3000)
    A1.deposit(3000)
    A1.deposit(3000)
    A1.deposit(3000)
    A1.deposit(3000)
    A1.withdraw(2000)
    A1.print_info()
    #print(A3.account_nums)

if __name__ == "__main__":
    main()

