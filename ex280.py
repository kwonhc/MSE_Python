#import random

#class Account:
#    account_count = 0
    
#    def __init__(self, name, balance):
#        self.deposit_count = 0
#        self.deposit_log = []
#        self.withdraw_log = []
        
#        self.name = name
#        self.balance = balance
#        self.bank = "광주은행"
        
#        num1 = random.randint(0, 999)
#        num2 = random.randint(0, 99)
#        num3 = random.randint(0, 999999)
        
#        num1 = str(num1).zfill(3)
#        num2 = str(num2).zfill(2)
#        num3 = str(num3).zfill(6)
#        self.account_number = num1 + '-' + num2 + '-' + num3
#        Account.account_count +=1
        
#    def get_aaccount_num(cls):
#        print(cls.account_count)
        
#    def deposit(self, amount):
#        if amount >= 1:
#            self.deposit_log.append(amount)
#            self.balance += amount
            
#            self.deposit_count += 1
#            if self.deposit_count %5 == 0:
#                self.balance = (self.balance * 1.01)
                
#    def withdraw(self, amount):
#        if self.balance > amount:
#            self.withdraw_log.append(amount)
#            self.balance -= amount
    
#    def display_info(self):
#        print("은행이름", self.bank)
#        print("예금주: ", self.name)
#        print("계좌번호: ", self.account_number)
#        print("잔고: ", self.balance)
    
#    def withdraw_history(self):
#        for amount in self.withdraw_log:
#            print(amount)
    
#    def deposit_history(self):
#        for amount in self.deposit_log:
#            print(amount)

#k = Account("Kwon", 100000000)
#k.deposit(2150000)
#k.deposit(5000000)
#k.deposit(40000000)
#k.deposit_history()

#k.withdraw(20000000)
#k.withdraw(6500000)
#k.withdraw_history()










        
            