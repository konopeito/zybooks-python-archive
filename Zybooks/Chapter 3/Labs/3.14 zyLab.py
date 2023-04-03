# 3.14.1: LAB: Input and formatted output: Right-facing arrow
base_char = input()
head_char = input()

row1 = '      ' + head_char
row2 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char
row3 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char + head_char
row4 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char
row5 = '      ' + head_char


print(row1)
print(row2)
print(row3)
print(row2)
print(row1)