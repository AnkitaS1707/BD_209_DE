balance = 100000
amount = float(input('Enter Ampount to withdraw: '))
if amount > balance:
    print ('Opps..Insufficient Balance')
else:
    balance = balance - amount
    print (f'Withdrawal successful, New Balance is:{balance}')