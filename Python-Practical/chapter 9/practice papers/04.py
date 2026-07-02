#a file contains a word "Donkey" multiple times.you need to
# write a pgm which replaxe this word with #### by updating the same file.

word="Donkey"

with open("Donkey.txt","r") as f:
    content=f.read()
    
contentNew=content.replace(word,"######")

with open("Donkey.txt","w") as f:
    f.write(contentNew)