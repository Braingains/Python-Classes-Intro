class BankAccount:

    def __init__(self, holder_name, balance, type):
        self.holder_name = holder_name
        self.balance = balance
        self.type = type #type is technically a keyword, but you can still use it        
        self.__rates = { #adding two underscores before the name makes it hidden from outside observers and unchangeable
            "personal" : 10,
            "business" : 50
        }

    def pay_in(self, amount):
        self.balance += amount

    def pay_monthly_fee(self):
        # if self.type == "business":
        #     self.balance -= 50
        # elif self.type == "personal":  
        #     self.balance -= 10
        self.balance -= self.__rates[self.type]

# def get_account_name(account):
#     return account["holder_name"]

    