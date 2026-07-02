#write a pgm to find out the line number where python is present from qn 6


with open("log.txt")as f:
    lines=f.readlines()
    
lineno=1
for line in lines:
    if("python" in line):
        print(f"yes python is present.\n line no:{lineno}")
        break
    lineno +=1
else:
    print("no python is not present")