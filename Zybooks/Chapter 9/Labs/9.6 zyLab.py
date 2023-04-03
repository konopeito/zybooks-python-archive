# LAB ACTIVITY
# 9.6.1: LAB: Name format

user_input = input()
name = user_input.split(" ")

if(len(name)==3):
    
    first = name[0]
    middle = name[1]
    last = name[2]
    
    print(last + ", " + first[0] + "." + middle[0] + ".")

elif(len(name) == 2):

    first = name[0]
    middle = name[1]

    print(middle + ", " + first[0] + ".")

else:
    print("The input does not have the correct form")

