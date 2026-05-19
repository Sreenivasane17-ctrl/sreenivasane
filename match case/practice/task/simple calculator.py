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
