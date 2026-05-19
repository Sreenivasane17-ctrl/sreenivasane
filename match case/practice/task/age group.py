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
