from modules.bank_account import *

# account = {
#     "holder_name" : "John",
#     "balance" : 500,
#     "type" : "business"

# }

#print(get_account_name(account))

bank_account = BankAccount("John", 500, "business")
# print(bank_account.holder_name)
bank_account.holder_name = "Ada" #changes name stored in variable named bank_account from John to Ada

bank_account2 = BankAccount("Jenny", 500, "personal")
#here we create an instance of the class BankAccount and assigned it to the variable bank_account2

# print(bank_account.holder_name)
# print(bank_account.balance)
# print(bank_account.type)

# bank_account.pay_in(50)
# print(bank_account.balance)

# bank_account.pay_monthly_fee()
# print(bank_account.balance)

bank_account.pay_monthly_fee()
print(bank_account.balance)