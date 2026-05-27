"""
print("Welcome to World Bank")
a = 10000
x = int(input("Enter 1 to withdraw funds, Enter 2 to deposit funds, Enter 3 to check balance:"))
if(x==1):
    y = int(input("Enter amount to be withdrawed:"))
    if(y<=10000):
        print(f"₹{y}amount withdrawed from your account")
        print(f"Remaining amount in your account is: ₹{a-y}")
    else:
        print("Insufficient funds")
elif(x==2):
    y = int(input("Enter amount to be deposited:"))
    print(f"₹{y}amount deposited in your account")
    print(f"Remaining amount in your account is: ₹{a+y}")
elif(x==3):
    print(f"Balance amount in your account:₹{a}")
else:
    print("Invalid Choice")

print("Area of Triangle")
b = float(input("Enter value for base of the triangle:"))
h = float(input("Enter value for height of the triangle:"))
area = 0.5*b*h
print(f"The area of the triangle is {area}sq.units")

print("Welcome to Happy Mall Cinemas")
age = int(input("Enter your age:"))
if(age<0):
    print("Invalid age")
elif(0<age<10):
    print("The cost of your ticket is ₹60")
elif(age<60):
    print("The cost of your ticket is ₹120")
else:
    print("The cost of your ticket is ₹80")

print("Check Leap Year Calculator")
year = int(input("Enter the year:"))
if(year%4==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap

print("Type of Triangle Checker")
a = float(input("Enter value of side a"))
b = float(input("Enter value of side b"))
c = float(input("Enter value of side c"))
if(a==b and b==c and a==c):
    print("The given triangle is an equilateral triangle")
elif(a==b or b==c or a==c):
    print("The given triangle is an isosceles triangle")
else:
    print("The given triangle is a scalene triangle")

db_useremail = "user01"
db_password = "1234"
email = input("Enter your email:")
password = input("Enter password:")
if((email !=" ") and (password !=" ")):
    if(email==db_useremail):
        if(password==db_password):
            print("Login Successful")
        else:
            print("Invalid Password")
    else:
        print("User not found")
else:
    print("Enter valid credentials")
"""
db_pin = 1234
account_balance = int(input("Enter your account balance:"))
withdrawal_amount = int(input("Enter your withdrawal amount:"))
pin = int(input("Enter your PIN"))
if(pin==db_pin):
    if(withdrawal_amount<=account_balance):
        if(withdrawal_amount%100==0):
            print("Withdrawal success")
        else:
            print("invalid denomination")
    else:
        print("insufficient balance")
else:
    print("Wrong PIN")