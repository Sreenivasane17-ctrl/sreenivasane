var=input("Enter the variable:")
match var:
    case var if var in "a,e,i,o,u,A,E,I,O,U":
        print("var in vowel")
    case var if var not in "a,e,i,o,u,A,E,I,O,U":
        print("var is constant")
    case _:
        print("invalid")
