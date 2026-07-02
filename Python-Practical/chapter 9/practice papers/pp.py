# # # def generatetable(n):
# # #     table=""
# # #     for i in range(1,11):
        
# # #         table +=f"{n}X{i}={n*i}\n"
# # #     with open(f"multip_{n}.txt","w") as f:
# # #         f.write(table)
            
# # # for i in range(2,21):
# # #     generatetable(i)
    
# # # # def generatetable(n):
# # # #     table=""
# # # #     for i in range(1,11):
# # # #         table += f"{n} X {i} = {n*i}\n"
        
# # # #     with open(f"tables/table_{n}.txt","w")as f:
# # # #         f.write(table)
        
# # # # for i in range(2,21):
# # # #     generatetable(i


# # word="donkey"

# # with open(f"donkey1.txt","r")as f:
# #     content=f.read()

# # newcontent=content.replace("donkey","######")

# # with open(f"donkey1","w")as f:
# #     f.write(newcontent)


# with open("log1.txt","r")as f:
#     content=f.read()
    
# if("python" in content):
#     print("word is presint")
# else:
#     print("not present")


with open("log1.txt","r")as f:
     content=f.read()
    
if("python" in content):
     print("word is presint")
else:
     print("not present")

