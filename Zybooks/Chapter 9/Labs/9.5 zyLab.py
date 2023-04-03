# 9.5.1: LAB: Checker for integer string
string = input()
result = True
for value in string:

    # checking value is not a digit
    if value < '0' or value > '9':
        result = False

if result:
    print("Yes")

else:
    print("No")
