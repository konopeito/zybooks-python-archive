# LAB ACTIVITY
# 3.15.1: LAB: Phone number breakdown

phone_number = int(input())

zip_code = int(phone_number // 10000000)
first_three = int((phone_number//10000) % 1000)
last_four = int(phone_number % 10000)

print('({:d}) {:d}-{:d}'.format(zip_code, first_three, last_four))