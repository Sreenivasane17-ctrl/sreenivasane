#Q1- write a program to count the number of vowels  in given


words=input("enter the letter:")
count=0
for i in words:
    if i.lower() in "aeiou":
        count+=1
    print("vowels:",count)
        
