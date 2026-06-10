# Exceptional handling

try:
    # ZeroDivisionError
    print(10 / 0)

    # ValueError
    x = int("abc")

    # NameError
    print(y)

    # IndexError
    lst = [1, 2, 3]
    print(lst[5])

    # KeyError
    d = {"name": "John"}
    print(d["age"])

    # TypeError
    print("10" + 5)

    # FileNotFoundError
    f = open("sample.txt", "r")

except ZeroDivisionError:
    print("ZeroDivisionError occurred")

except ValueError:
    print("ValueError occurred")

except NameError:
    print("NameError occurred")

except IndexError:
    print("IndexError occurred")

except KeyError:
    print("KeyError occurred")

except TypeError:
    print("TypeError occurred")

except FileNotFoundError:
    print("FileNotFoundError occurred")

finally:
    print("Program completed")