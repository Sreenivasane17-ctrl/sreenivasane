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
