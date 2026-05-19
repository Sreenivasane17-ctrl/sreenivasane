#Q11-count the no. of words in string without using split()

words = input("enter the words:").strip()
count=1
for ch in words:
    if ch ==" ":
        count += 1
print(count)
        
