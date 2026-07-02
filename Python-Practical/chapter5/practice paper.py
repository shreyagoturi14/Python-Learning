# #write pgm to create a dictionary of hindi words with values as the english translation.
# #provid use with an option to look up

# # word=input("Enter the word you want meaning of: ")
# # words={
# #     "mada":"help",
# #     "kursi":"chair",
# #     "billi":"cat"
# # }
# # # word=input("Enter the word you want meaning of: ")
# # print(words[word])

# # #write pgm t input eight number from the user and display all the unique number(once
# # a=set()
# # n=input("enter number: ")
# # a.add(int(n))
# # n=input("enter number: ")
# # a.add(int(n))
# # n=input("enter number: ")
# # a.add(int(n))
# # n=input("enter number: ")
# # a.add(int(n))
# # n=input("enter number: ")
# # a.add(int(n))
# # n=input("enter number: ")
# # a.add(int(n))
# # print(a)

# # #can we have a set with 18(int)and '18'(str)as a value in it?
# s=set()
# s.add(18)
# s.add("18")
# print(s)

# # what will be the length of the following
# s=set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(s)

# # #what is the type of s
# s={}
# print(type(s))

# # #create an empty dict .allow 4 friends to enter the favorite language as value and use key as thir same . assume that the name are nique
# # # s={}
# # # name=input("enter friends name: ")
# # # lang=input("Enter the lang name: ")
# # # s.update({name:lang})
# # # name=input("enter friends name: ")
# # # lang=input("Enter the lang name: ")
# # # s.update({name:lang})
# # # name=input("enter friends name: ")
# # # lang=input("Enter the lang name: ")
# # # s.update({name:lang})
# # # name=input("enter friends name: ")
# # # lang=input("Enter the lang name: ")
# # # s.update({name:lang})
# # # print(s)

#can you change the value inside a list  which is conntained in a set
s=(8,7,12,"shreya",[1,2])
print(s)   # no it can not change list is not hashable

s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)
