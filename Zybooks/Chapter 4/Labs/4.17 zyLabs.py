# LAB ACTIVITY
# 4.17.1: LAB: Exact change
change = int(input())

if(change > 0):
    if(change >= 100):
        dollars = int(change / 100)
        change = change % 100
        if(dollars == 1):
            print('1 Dollar')
        else:
            print(f'{dollars} Dollars')

    if(change >= 25):
        quarters = int(change / 25)
        change = change % 25
        if(quarters == 1):
            print('1 Quarter')
        else:
            print(f'{quarters} Quarters')

    if(change >= 10):
        dimes = int(change / 10)
        change = change % 10
        if(dimes == 1):
            print('1 Dime')
        else:
            print(f'{dimes} Dimes')

    if(change >= 5):
        nickels = int(change / 5)
        change = change % 5
        if(nickels == 1):
            print('1 Nickel')
        else:
            print(f'{nickels} Nickels')

    if(change > 0):
        pennies = change
        if(pennies == 1):
            print('1 Penny')
        else:
            print(f'{pennies} Pennies')
else:
    print('No change') 
