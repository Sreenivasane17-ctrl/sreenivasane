#Q7-count how many digits in string

nums=input("enter your numbers:")
count=0
for i in nums:
    if i.isdigit():
        count+=1
print(count)
    

