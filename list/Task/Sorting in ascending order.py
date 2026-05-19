#Q19-Check a list sorted in ascending order

list=[34,78,9,43]
asc=list[0]
for i in list:
    if i<= asc:
        asc=i
    else:
        print("it is not sorted")
        break
print("it is sorted in ascending in order")
