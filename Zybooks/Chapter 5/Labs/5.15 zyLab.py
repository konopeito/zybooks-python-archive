# LAB ACTIVITY
# 5.15.1: LAB: Password modifier
word = input()
password = ''
i = 0

while i < len(word):
    if word[i]=='i':
       password +='1'
    elif word[i]=='a':
       password +='@'
    elif word[i]=='m':
       password +='M'
    elif word[i]=='B':
       password +='8'
    elif word[i]=='s':
       password +='$'
    else:
        password += word[i]
    i +=1
password = password + '!'
print(password)