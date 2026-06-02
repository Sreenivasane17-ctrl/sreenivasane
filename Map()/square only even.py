list1=[1,2,3,4,5,6]
result=list(filter(lambda x:x%2==0,list1))
result=map(lambda x:x*x,result)
print(list(result))
