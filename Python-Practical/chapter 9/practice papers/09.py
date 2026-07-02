#write a pgm to find out the whether the file is identicle & 
# matches the contents of another file

with open("file1.txt")as f:
     content1=f.read()
 
with open("file2.txt")as f:
     content2=f.read()
     
if(content1==content2):
    print("yes these files are identical")
else:
    print("no these are not identicle")