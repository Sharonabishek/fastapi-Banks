from fastapi import FastAPI
app=FastAPI()

class Banks:
    def __init__(self,name,account_num,balance_amount):
        self.name = name
        self.account_num = account_num
        self.balance_amount = balance_amount

    def deposit(self,amount):
        self.balance_amount+= amount
        print(amount," was added to your account number ",self.account_num)
        print("Current balance: ",self.balance_amount)

    def withdraw(self,amount):
        if(self.balance_amount>=amount):
            self.balance_amount-=amount       
            print(amount," was debited from your account number ",self.account_num)
            print("Current balance: ",self.balance_amount)
        else:
            print("//No money found to withdraw//")  
            print("Current balance: ",self.balance_amount)

    '''def balance_check(self,account_num):
        print("Name: ",self.name)
        print("Account Number: ",self.account_num)
        print("Balance ",self.balance_amount)
    '''
accounts=[]

@app.post('/newaccount')
def create_account(name :str,account_num :int,balance_amount :float):
    accounts.append(Banks(name,account_num,balance_amount))
    response={}
    response.update({"Username ":accounts[-1].name,"Account number ":accounts[-1].account_num,"Current Balance ":accounts[-1].balance_amount})  
    return response


@app.get('/deposit')
def deposit_money(amount :int,account_num :int):
    results=[]
    print("Account number: ",account_num)
    for user in accounts:
        if (user.account_num ==account_num):  
            user.deposit(amount)
            results.append({"Name ":user.name,"Account Number ":user.account_num,"Balance ":user.balance_amount})
    return results        

@app.get('/withdraw')
def withdraw_money(amount :int,account_num :int):
    results=[]
    print("Account number: ",account_num)
    for user in accounts:
        if (user.account_num ==account_num):  
            user.withdraw(amount)
            results.append({"Name ":user.name,"Account Number ":user.account_num,"Balance ":user.balance_amount})
    return results            


@app.get('/accountinfo')
def check_money(account_num :int):
    results={}
    for user in accounts:
        if (user.account_num ==account_num):  
            results.update({"Name ":user.name,"Account Number ":user.account_num,"Balance ":user.balance_amount})
    return results                