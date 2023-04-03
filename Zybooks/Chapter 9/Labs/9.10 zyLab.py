# LAB ACTIVITY
# 9.10.1: LAB: Remove all non-alpha characters
user_string = input()

alpha_only_string = ""

for x in user_string:
    if "A" <= x <= "Z" or "a" <= x <= "z":
       alpha_only_string += x

print(alpha_only_string)