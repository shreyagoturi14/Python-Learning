# write program to mine a log file and find out whether it contains 'python.'

#1
f=open("log.txt")

contant=f.read()
if("python" in contant):
    print("python word is present")
else:
    print("python word is not present")
f.close()

#2
with open("log.txt")as f:
    content=f.read()
if("python in content"):
    print("python word is present")
else:
    print("no python word is present")