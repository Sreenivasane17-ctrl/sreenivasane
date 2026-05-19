#Q2 rev a string using a loop

name=input("enter a string:")
rev=""
for ch in name:
    rev=ch+rev
print("reverse of string is",rev)
    
