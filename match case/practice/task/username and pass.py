user=input("enter username:")
passwd=input("enter password:")
match(user,passwd):
    case ("MCacc","2026"):
        print("Login successful")
    case ("MCacc",_):
        print("invalid password")
    case _:
        print("invalid username")
