# LAB ACTIVITY
# 5.18.1: LAB: Brute force equation solver
a = int(input())
b = int(input())
c = int(input())


d = int(input())
e = int(input())
f = int(input())

for x in range(-10, 12, 1):
    for y in range(-10, 12, 1):
        if (a*x + b*y == c) and (d*x + e*y == f):
            print('x =', x, ',', 'y =', y)
            break
    if (a*x + b*y == c) and (d*x + e*y == f):
        break

    elif  x == 11 and y == 11:
        print("There is no solution")