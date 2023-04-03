# 6.23.1: LAB: Fibonacci sequence
def fibonacci(n):
    if n < 0:
        return -1
    
    a = 0
    b = 1
    c = 0
    for i in range(n - 1):
        c = a + b
        a, b = b, c
    
    return c

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')