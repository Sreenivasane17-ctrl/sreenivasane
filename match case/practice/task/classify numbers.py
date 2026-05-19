n1=int(input("Enter the number:"))
match n1:
    case 0:
        print("zero")
    case n1 if n1 % 2 == 0:
        print("Positive numbers")
    case _:
        print("Negative numbers")
