num=int(input("enter the number:"))
match num:
    case num if 1<=num<=10:
        print("the number is between 1 to 10")
    case _:
        print("the number is not between 1 to 10")
