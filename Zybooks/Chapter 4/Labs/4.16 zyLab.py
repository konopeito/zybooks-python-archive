# 4.16.1: LAB: Seasons
input_month = input()
input_day = int(input())

spring = ['March', 'April', 'May', 'June'] #March 20 - June 20
summer = ['June', 'July', 'August', 'September'] #June 21 - September 21
autumn = ['September', 'October', 'November', 'December'] #September 22 - December 20
winter = ['December', 'January', 'February', 'March'] #December 21 - March 19

months_with_30 = ['April', 'June', 'September', 'November']
months_with_31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
february = ['February'] #is special with 28 or 29 days

#checks if input_month is a valid month
valid_month = ((input_month in spring) or 
               (input_month in summer) or 
               (input_month in autumn) or 
               (input_month in winter))
#checks if input_day is valid for input_month
valid_day = (((input_month in months_with_31) and (input_day > 0 and input_day <= 31)) or
             ((input_month in months_with_30) and (input_day > 0 and input_day <= 30)) or
             ((input_month in february)       and (input_day > 0 and input_day <= 29)))

if(valid_month and valid_day):
    if  (input_month in spring):
        if(input_month == spring[0]): #checks if March
            if(input_day >= 20):
                print('Spring')
            else: 
                print('Winter')
        elif(input_month == spring[1] or input_month == spring[2]): #checks if April or May
            print('Spring')
        else: #is June
            if(input_day <= 20):
                print('Spring')
            else:
                print('Summer')

    elif(input_month in summer): #June has already been covered by Spring so don't need to check it again
        if(input_month == summer[3]): #checking if September
            if(input_day <= 21):
                print('Summer')
            else:
                print('Autumn')
        else: #is July or August
            print('Summer')

    elif(input_month in autumn): #September has already been covered by Summer so don't need to check it again
        if(input_month == autumn[3]): #checks if December
            if(input_day <= 20):
                print('Autumn')
            else: #is October or November
                print('Winter')
        else:
            print('Autumn')

    else: #Winter. Both December and March have been covered so must be winter
        print('Winter')
else:
    print('Invalid')