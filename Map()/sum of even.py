from functools import reduce

even=[1,2,3,4,5,6]
result=list(filter(lambda x:x%2==0,even))
result=reduce(lambda x,y:x+y,result)
print(int(result))