num = int(input("enter the no:"))
match num:
    case num if num == 0:
        print(f"{num} the given num is zero")
    case num if num <= 0:
        print(f"{num} the given num is -ve")
    case num if num >= 0:
        print(f"{num} the given num is +ve")
