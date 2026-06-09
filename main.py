def bank_account():
    balance = 1000
    
    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return balance
        else:
            return 'Insufficient funds'
    
    print(withdraw(200))
    print(withdraw(900))
    print(withdraw(100))

bank_account()