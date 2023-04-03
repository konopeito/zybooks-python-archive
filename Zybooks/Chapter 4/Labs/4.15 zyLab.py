
# 4.15.1: LAB: Interstate highway numbers
highway_number = int(input())

if(highway_number > 0) and (highway_number <= 999) and (highway_number % 100 != 0): #valid range
    if(highway_number % 2 == 0): #checks even
        if(highway_number < 100): #primary
            print(f'I-{highway_number} is primary, going east/west.')
        else: #auxiliary
            print(f'I-{highway_number} is auxiliary, serving I-{highway_number % 100}, going east/west.')
    else: #is odd
        if(highway_number < 100): #primary
            print(f'I-{highway_number} is primary, going north/south.')
        else: #auxiliary
            print(f'I-{highway_number} is auxiliary, serving I-{highway_number % 100}, going north/south.')
else:
    print(f'{highway_number} is not a valid interstate highway number.') 

