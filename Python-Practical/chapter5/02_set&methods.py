s={1,3,44,44,44,5}

e=set() #dont use s={} as it will create an empty dictionary it does't create empty list
print(s) #it dont take repeated value
s.add(322)  #add
print(s,type(s)) 
s.remove(1)#remove
print(s)
s.clear()
print(s)


s1={1,33,76}
s2={34,67,33}
print(s1.union(s2))
print(s1.intersection(s2))