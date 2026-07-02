#reading a file 
#open the file in readd mode
f = open("file.txt","r")
#read its contents
data = f.read()
#print its contents
print(data)
#close the file 
f.close()

# with open("file.txt","r")as f:
#     data=f.read()
# print("contents of file .txt are: ")
# print(data)