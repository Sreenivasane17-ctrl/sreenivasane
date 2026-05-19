#Q8-How many -ve numbers from list

list=[10,-20,31,78,-45]
count=0
for i in list:
    if i<0:
        count += 1
print(count)
