# LAB ACTIVITY
# 6.20.1: LAB: Step counter
def feet_to_steps(user_feet):
    steps_walked = user_feet / 2.5
    return int(steps_walked)

if __name__ == '__main__':

    input_feet = float(input())
    steps_walked = feet_to_steps(input_feet)
    print(int(steps_walked))
 