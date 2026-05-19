#Max_min

tuple_1=(4,8,1,7)
max=tuple_1[0]
min=tuple_1[0]
for i in tuple_1:
    if i < min:
        min = i
    elif i > max:
        max = i
print("the max value is",max)
print("the min value is",min)
