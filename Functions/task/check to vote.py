#Q3- check eligible to vote

age=int(input("Enter your age:"))

def vote(age):

    if(age>=18):
        print("Your eligible to vote")
    else:
        print("Your not eligible to vote")

vote(age)