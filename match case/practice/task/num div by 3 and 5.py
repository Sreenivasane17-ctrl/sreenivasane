x=int(input("Enter the number:"))
match x:
    case x if x % 3 == 0 and x % 5 == 0:
        print("The x value divisible by 3 & 5")
    case _:
        print("The x value not divisible by 3 & 5")
