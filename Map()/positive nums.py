mylist=[-5,-2,0,3,8]
def pos(x):
    if x > 0:
        return x
num=filter(pos,mylist)
print(list(num))