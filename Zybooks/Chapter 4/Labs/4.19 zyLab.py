# 4.19.1: LAB: Golf scores
par = int(input())
strokes = int(input())

if(par >= 3 and par <= 5):
    if(strokes == par - 2):
        print('Eagle')
    if(strokes == par - 1):
        print('Birdie')
    if(strokes == par):
        print('Par')
    if(strokes == par + 1):
        print('Bogey')
else:
    print('Error')