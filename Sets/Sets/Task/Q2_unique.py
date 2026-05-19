#Q2-create a set of unique words  from a sentence where words are separated by spaces and punctuation marks 
# should be ignored

a="Welcome to python programming"
b=a.lower().split()
unique=set()
for i in b:
    if i not in ("!@#%^&()-=_+"):
        unique.add(i)
print(unique)
