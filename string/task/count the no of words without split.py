#Q11-write a program to count the no. of words in string without using split()

word=input("enter the sentence:")
res=1
for ch in word:
    if ch == " ":
        res += 1
print(word)
