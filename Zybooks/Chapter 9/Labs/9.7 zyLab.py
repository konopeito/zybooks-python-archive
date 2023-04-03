# LAB ACTIVITY
# 9.7.1: LAB: Count characters
input_data = input()
character = input_data[0]
phrase = input_data[1:]
count = 0

for char in phrase:
    if char == character:
        count = count + 1
if  count == 1:

    print(count,character)

else:
     
    print(count,str(character)+"'s")
