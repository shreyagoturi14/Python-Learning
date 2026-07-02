#1 write a pgm to find the greatest of four number entered by user
a1=int(input("Enter number 1: "))
a2=int(input("Enter number 2: "))
a3=int(input("Enter number 3: "))
a4=int(input("Enter number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("greatest number is a1: ",a1)
    
elif(a2>a1 and a2>a3 and a2>a4):
    print("greatest number is a2: ",a2)
    
if(a3>a1 and a3>a2 and a3>a4):
    print("greatest number is a3: ",a3)
    
if(a4>a2 and a4>a3 and a4>a1):
    print("greatest number is a1: ",a4)
    
    
    
#2 write pgm to find out whther the stu is passed or failed 
#if it requers total of 40% and atleast 33%in each sub to pass
#assume 3 subs and take marks as an input
sub1=int(input("Enter the marks1: "))
sub2=int(input("Enter the marks2: "))
sub3=int(input("Enter the marks3: "))

#check for total percentage
total_percentage=(100*(sub1+sub2+sub3))/300

if(total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("you are passed:",total_percentage)
else:
    print("you are failed:",total_percentage)
    
    
    
#3 a spam comments is defined as a text containing following kry words
#"Make a lot of money","buy now","subscription","click this"
#write pgm to delete these spams
p1="Make a lot of money"
p2="buy now"
p3="subscription"
p4="click this"

message=input("Enter your comment: ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")
else:
    print("This comment is not a spam")
    
    
#4 write pgm t find whether a given username contain less than 10 character or not 
user_name=input("enter the character: ")
if(len(user_name)<10):
     print("your user_name contains less than 10 characters")
else:
    print("your username contain more than 10 characters")
    
    
#5 write pgm to find out whether given name is present in a list or not
l=["shreya","nisha","pooja","spoorti"]
name=input("Enter your name: ")
if(name in l):
    print("your name in the list")
else:
    print("your name is not in the list")
    
    
#6 write pgm to calc the grade of a student from his marks from the following
#90-100=>EX
#80-90=>A
#70-80=>B
#60-70=>C
#50-60=>D
#<50=>F
marks=int(input("Enter your marks: "))
if(marks<=100 and marks>=90):
    grade="EX"
elif(marks<90 and marks>=80):
    grade="A"
elif(marks<80 and marks>=70):
    grade="B"
elif(marks<70 and marks>=60):
    grade="C"
elif(marks<60 and marks>=50):
    grade="D"
elif(marks<50):
    grade="F"
print("your grade is: ",grade)


#7 write a pgm to find out whether given post is talking about "shreya" or not
post=input("Enter the post: ")
if("Shreya" .lower() in post.lower()):
    print("This post is talking about Shreya")
else:
    print("This post is not talking about Shreya")