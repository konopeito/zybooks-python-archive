# LAB ACTIVITY
# 2.14.1: LAB: Driving costs
miles_per_gallon=float(input())
dollars_per_gallon=float(input())
dollars_per_mile=dollars_per_gallon*1/miles_per_gallon

miles_20= 20*dollars_per_mile
miles_75=75*dollars_per_mile
miles_500=500*dollars_per_mile
print(f'{miles_20:.2f} {miles_75:.2f} {miles_500:.2f}')