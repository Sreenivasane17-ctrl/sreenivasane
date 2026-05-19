#Q3-string is palindrome using a loop 



name=input("enter a string:")
rev=""
for ch in name:
    rev=ch+rev
print("reverse of string is",rev)
if name==rev:
    print("it is palindrome")
else:
    print("it is not palindrome")
