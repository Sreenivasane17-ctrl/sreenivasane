#Q12-Replace all -ve number in a list with 0

list1=[45,12,-80,78,-30,36]
for i in range(len(list1)):
    if list1[i]<0:
        list1[i]=0
print(list1)
