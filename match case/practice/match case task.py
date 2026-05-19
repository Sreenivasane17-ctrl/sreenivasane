#Q1


'''even_odd = int(input(" enter the num to be checked:"))
match even_odd:
    case even_odd if even_odd % 2 == 0:
        print(f"{even_odd} the num is even")
    case even_odd if even_odd % 2 != 0:
        print(f"{even_odd} the num is odd")

#Q2


num = int(input("enter the no:"))
match num:
    case num if num == 0:
        print(f"{num} the given num is zero")
    case num if num <= 0:
        print(f"{num} the given num is -ve")
    case num if num >= 0:
        print(f"{num} the given num is +ve")
#Q3


data = input("enter the operation:")
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
match data:
    case data if data == "add":
        print(num1+num2)
    case data if data == "sub":
        print(num1-num2)
    case data if data == "multipy":
        print(num1*num2)
    case data if data == "div":
        print(num1/num2)


#Q4



day=input("enter the day:")
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("it is weekday")
    case "saturday" | "sunday":
        print("it is weekend")
    case _:
        print("invalid day")

#Q5


marks = int(input("Enter the marks:"))
match marks:
    case marks if marks >=90:
        print("Grade A")
    case marks if marks >=70:
        print("Grade B")
    case marks if marks >=50:
        print("Grade C")
    case marks if marks >=35:
        print("Grade D")
    case _:
        print("invalid")



#Q6


month = int(input("Enter the month"))
match month:
    case month if month == 1:
        print("January")
    case month if month == 2:
        print("Febraury")
    case month if month == 3:
        print("March")
    case month if month == 4:
        print("April")
    case month if month == 5:
        print("May")
    case month if month == 6:
        print("June")
    case month if month == 7:
        print("July")
    case month if month == 8:
        print("August")
    case month if month == 9:
        print("September")
    case month if month == 10:
        print("October")
    case month if month == 11:
        print("November")
    case month if month == 12:
        print("December")
    case _:
        print("invalid")



#Q7


var=input("Enter the variable:")
match var:
    case var if var in "a,e,i,o,u,A,E,I,O,U":
        print("var in vowel")
    case var if var not in "a,e,i,o,u,A,E,I,O,U":
        print("var is constant")
    case _:
        print("invalid")




#Q8


signal=input("enter the colour:")
match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Get ready")
    case "green":
        print("Go")
    case _:
        print("invalid")




#Q9



year=int(input("Enter the year:"))
match year:
    case year if year % 4 == 0:
        print("it is leap year")
    case year if year % 4 != 0:
        print("it is not leap year")
    case _:
        print("invalid")



#Q10


age=int(input("enter your age:"))
match age:
    case age if age <=12:
        print("child")
    case age if age <=19:
        print("teenager")
    case age if age <=59:
        print("Adult")
    case _:
        print("senior citizen")

#Q11




num=int(input("enter the number:"))
match num:
    case num if 1<=num<=10:
        print("the number is between 1 to 10")
    case _:
        print("the number is not between 1 to 10")





#Q12


user=input("enter username:")
passwd=input("enter password:")
match(user,passwd):
    case ("MCacc","2026"):
        print("Login successful")
    case ("MCacc",_):
        print("invalid password")
    case _:
        print("invalid username")




#Q13



sides=int(input("enter number of sides:"))
match sides :
    case 0:
        print("circle")
    case 3:
        print("triangle")
    case 4:
        print("square")
    case 5:
        print("pentagon")
    case 6:
        print("hexagon")
    case 7:
        print("heptagon")
    case 8:
        print("octogon")
    case _:
        print("shape not identified")
    


#Q14


x=int(input("Enter the number:"))
match x:
    case x if x % 3 == 0 and x % 5 == 0:
        print("The x value divisible by 3 & 5")
    case _:
        print("The x value not divisible by 3 & 5")





#Q15


n1=int(input("Enter the number:"))
match n1:
    case 0:
        print("zero")
    case n1 if n1 % 2 == 0:
        print("Positive numbers")
    case _:
        print("Negative numbers")'''





a=0
for i in range(1,11):
    a=a+i
print(a)





















        
        

















        






































        
    
    
    
