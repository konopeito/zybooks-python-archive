# LAB ACTIVITY
# 5.14.1: LAB: Convert to reverse binary
number = int(input())

binary_number = ''

while number // 2 != 0:
    if number % 2 == 1:
        binary_number += '1'
    if number % 2 == 0:
        binary_number += '0'
    number = number // 2
    if number // 2 == 0:
        binary_number += '1'
else:
    print(binary_number)
