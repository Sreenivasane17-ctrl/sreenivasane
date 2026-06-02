from functools import reduce# 1. Double All Numbers

list1=[1, 2, 3, 4, 5]
result = list(filter(lambda x:x%2!=0 ,list1))
result=map(lambda x:x*x ,result)
result=reduce(lambda x,y:x+y ,result)
print (int(result))
