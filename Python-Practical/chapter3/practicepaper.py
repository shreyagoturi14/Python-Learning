#1write py pgm to display user entered name followed by good afetrnoon using input()fun
name=input("enter  the name: ")
print(f"good afternoon {name}")

#2
letter='''Dear<|Name|>,
you are selected!
<|Date|>'''
print(letter.replace("<|Name|>","shreya").replace("<|Date|>", "24 sep 2050"))


#3 find the detect double space in astring
name="Shreya your    ..."
print(name.find(" "))
print(name.find("  "))

#4replace double space into single space
name="Shreya your    ..."
print(name.replace("  "," "))#strings are immutable which means that you cannot change them by running funs on them


#5
print("latter=Dear\tHarry,\tThis\tpython\tcource\tis\tnice")
