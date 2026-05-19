year=int(input("Enter the year:"))
match year:
    case year if year % 4 == 0:
        print("it is leap year")
    case year if year % 4 != 0:
        print("it is not leap year")
    case _:
        print("invalid")
