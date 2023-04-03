# LAB ACTIVITY
# 9.9.1: LAB: Palindrome

user_string = input()
no_space_string = user_string.replace(" ","")

if no_space_string == no_space_string[::-1]:
    print(f'{"palindrome:"} {user_string}')
else:
    print(f'{"not a palindrome:"} {user_string}')