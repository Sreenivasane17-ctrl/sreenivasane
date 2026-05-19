#Q8-string contains only alphabetics characters (without using isalpha())

words=input("enter the string:")
al=True
for ch in words:
    if not((ch>='A' and ch <='Z') or (ch>='a' and ch <= 'z')):
        al = False
        break
if al:
    print("full of alphabets")
else:
    print("No alphabets")
    
