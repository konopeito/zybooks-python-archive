# LAB ACTIVITY
# 6.22.1: LAB: Swapping variables
def swap_values(val1, val2, val3, val4):
    print(f'{val2} {val1} {val4} {val3}')
    return val2, val1, val4, val3

if __name__ == '__main__': 
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    
    swap_values(a, b, c, d)