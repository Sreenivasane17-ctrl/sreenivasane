#Q10-count hoe many even and odd no are present in list


lst=[12,54,32,78,10]
odd=0
even=0
for i in lst:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("No. of even number:",even)
print("No. of odd number:",odd)
