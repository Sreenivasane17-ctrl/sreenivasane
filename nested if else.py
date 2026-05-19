#Q1-account details

db_act = "17170001717171618"
db_pin = "1718"
db_savings = "10000"

user_act = int(input("Enter your acccount number:"))
user_pin = int(input("Enter your pin:"))

if(db_act==user_act):
   if(db_pin==user_pin):
       user_savings = int(input("Enter the amount:"))
       if(db_savings >= user_savings):
            print("Amount withrawed")
       else:
            print("Insufficient amount")
   else:
        print("Invalid pin")
else:
    print("Inavalid account")

#Q2- Gmail account

db_email="sree1gr@gmail.com"
db_passwd="sree134"
user_email=input("Enter your email")
user_passwd=input("Enter the passwd")
if(db_email==user_email):
    if(db_passwd==user_passwd):
        print("Login successful")
    else:
        print("Login unsuccessful")
else:
    print("Login unsuccessful")
