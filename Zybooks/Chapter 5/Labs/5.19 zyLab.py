# 5.19 LAB: Adjust values in a list by normalizing
length_list = int(input())
height_list = []
largest_height = 0
i = 0
while i < length_list:
    height = float(input())
    height_list.append(height)
    i += 1

    if largest_height < height:
        largest_height = height

for height in height_list:
    normalized_height = height / largest_height
    print('{:.2f}'.format(normalized_height))