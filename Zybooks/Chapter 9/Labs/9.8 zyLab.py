# LAB ACTIVITY
# 9.8.1: LAB: Mad Lib - loops
user_input = input()
words = user_input.split()
while words[0] != "quit":
 print("Eating", words[1], words[0], "a day keeps you happy and healthy.")
 user_input = input()
 words = user_input.split()