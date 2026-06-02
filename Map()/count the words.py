
list1=["cat", "apple", "dog", "banana"]
def count(word):
    for l in range (len(list1)):
        x=list1[l]
        if len(x)>3:
            word=word+1
    return word
print(count(0))
