# LAB ACTIVITY
# 5.16.1: LAB: Output range with increment of 5
x = int(input())
y = int(input())

if x <= y :
    for i in range (x, y+1, 5):
        print(i, end=' ')
    print()
else:
    print('Second integer can\'t be less than the first.')