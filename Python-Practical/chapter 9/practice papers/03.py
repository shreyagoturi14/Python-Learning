#write a pgm to generate multiplication table from 2 to 20 
#and write it to the different files. place these files in a 
# folder for a 13 -year old.

# n=int(input("enter the number: "))   
# def multiply(n):
#     for i in range(2,21):
#         print(f"{n}X{i}={n*i}")
        
# multiply(n)

def generatetable(n):
    table=""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
        
    with open(f"tables/table_{n}.txt","w")as f:
        f.write(table)
        
for i in range(2,21):
    generatetable(i)