even_odd = int(input(" enter the num to be checked:"))
match even_odd:
    case even_odd if even_odd % 2 == 0:
        print(f"{even_odd} the num is even")
    case even_odd if even_odd % 2 != 0:
        print(f"{even_odd} the num is odd")
