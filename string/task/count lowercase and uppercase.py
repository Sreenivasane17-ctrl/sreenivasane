#Q4-count no of uppercase and lowercase letters in string

name=input("enter your name:")
uc=lc=0
for ch in name:
    if ch.isupper():
        uc+=1
    elif ch.islower():
        lc+=1
print("uppercase letters:",uc)
print("lowercase letters:",lc)
