# LAB ACTIVITY
# 2.15.1: LAB: Expression for calories burned during workout
''' Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368 '''

Age= int(input())
Weight= int(input())
HeartRate=int(input())
Time= int(input())
calories= ((Age * 0.2757) + (Weight * 0.03295) + (Heart Rate * 1.0781) — 75.4991) * Time / 8.368 
print(f'Calories: {calories:.2f} calories')