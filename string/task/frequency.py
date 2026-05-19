#Q6-find the frequency of each string



a=input("enter a string:")
for ch in a:
    if a.count(ch) == 1 or ch not in a[:a.index(ch)]:
        print(ch,":",a.count(ch))
