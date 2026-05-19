#Q10-characters located at even indices of string


name = input("enter the string: ")
result = ""
for i in range(len(name)):
    if i % 2 == 0:
        result += name[i]
print(result)
