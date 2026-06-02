from functools import reduce# 1. Double All Numbers

list2=[1, 2, 3, 4, 5, 6]
result = list(filter(lambda x:x%2==0 ,list2))
result=map(lambda x:x*x*x ,result)
result=reduce(lambda x,y:x+y ,result)
print(int(result))