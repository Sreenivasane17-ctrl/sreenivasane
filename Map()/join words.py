from functools import reduce

string=[" python "," is "," awesome "]
result=reduce(lambda x,y:x+y,string)
print(result)