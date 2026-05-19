#Q18- Second largest number

list0=[12,56,67,568]

lar=list0[0]
seclar=list0[0]
for i in list0:
    if i > lar:
        seclar = lar
        lar = i
    elif i > seclar and i != lar:
        seclar = i
print(seclar)
