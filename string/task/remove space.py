#Q5-remove all spaces from string without using in-built()

name = input("enter the string:")
no_space=""
for ch in name:
    if ch !=" ":
        no_space+=ch
print(no_space) 


