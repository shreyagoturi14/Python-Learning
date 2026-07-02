#write the pgm to read the text from a given file 'poems.txt,
# and find out whether it contains word 'twinkle'.

# f=open("poems.txt")
# data=f.read()
# print(data)
# f.close()  it just reads the contents


f=open("poems.txt")
content=f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")
else:
    print("The word twinkle is not present in the content")
f.close()