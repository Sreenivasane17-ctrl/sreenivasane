list2=[1,2,3,4,5,6]
def even_value (x):
    return x%2!=0
result=filter(even_value,list2)
print(list(result))