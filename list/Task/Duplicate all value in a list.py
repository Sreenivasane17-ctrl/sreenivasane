#Q15-Print all duplicate value in a list

list1=[10,10,45,58,23,23,50]
duplicates=[]
for i in list1:
    if list1.count(i)>1:
        duplicates. append(i)
print(duplicates)
                
