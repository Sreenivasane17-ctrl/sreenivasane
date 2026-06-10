'''from datetime import datetime,timedelta
def age(x,y):
    return x - y



cur_yy=int(input("enter current year:"))
dob=input("enter your dob:")
dob=dob[:4]
dob = int(dob)
a = age(cur_yy,dob)

def number (age):
    return age * 365
print(number(a))
'''
year = int(input("enter the year:"))
if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    print("leap year")
else:
    print(" not leap year")