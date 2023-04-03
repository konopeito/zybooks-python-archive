# LAB ACTIVITY
# 6.19.1: LAB: Driving costs - functions
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return dollars_per_gallon / miles_per_gallon * miles_driven


def input_compute_and_print():
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    miles = [10, 50, 400]
    for i in miles:
        print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, i):.2f}')


def print_example():
    cost = driving_cost(20.0,3.1599, 50.0)
    print(f'{cost:.2f}')