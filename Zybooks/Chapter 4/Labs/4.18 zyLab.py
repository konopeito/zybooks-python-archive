# 4.18.1: LAB: Leap year
is_leap_year = False
input_year = int(input())
is_leap_year = input_year % 4 == 0 if(input_year % 100 != 0) else input_year % 400 == 0

if(is_leap_year):
    print(f'{input_year} - leap year')
else:
    print(f'{input_year} - not a leap year')