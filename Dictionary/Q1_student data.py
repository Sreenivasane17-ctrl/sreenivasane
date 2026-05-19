#Write a Python program to process 10 student's details. The program should calculate the total marks of each student, assign ranks based on the highest total marks, and display the student’s name, total marks, rank, and comments.
#Display comments using the following conditions:

a=int(input("enter the value:"))               
student_Details = []
for i in range(a):
    d={}
    name=input("enter the name:")
    email=input("enter your email:")
    mobile=int(input("enter the mobile:"))
    mark=list(eval(input("enter the marks:")))

    d['name'] = name
    d['email']  = email
    d['mobile'] = mobile
    d['mark'] = mark
    d['total'] = sum(mark)
    student_Details.append(d)

student_Details.sort(key=lambda x:x['total'],reverse=True)
print(student_Details)
grade=1

for i in student_Details:
    if i['total']>=450:
        comment="excelent"
    elif i["total"]<450 and i['total']>=300:
        comment="good"
    elif i["total"]<300:
        commment="average"
    print("name:",i['name'],"/n","total",i['total'],"/n","Grade:",grade,"/n","Comments",comment)
grade+=1    
