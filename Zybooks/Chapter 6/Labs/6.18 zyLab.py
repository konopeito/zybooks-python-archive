# LAB ACTIVITY
# 6.18.1: Lab training: Unit tests to evaluate your program
def kilo_to_pounds(kilos):
    return kilos * 2.204

if __name__ == '__main__':
    kilos = float(input())
    pounds = kilo_to_pounds(kilos)
    print(f"{pounds} lbs")