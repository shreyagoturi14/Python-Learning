marks={
    "shreya":100,
    "nisha":99,
    "pooja":98,
    "spoorti":97
}
print(marks,(type(marks)))
print(marks,["shreya"]) 


marks={
    "shreya":100,
    "goturi":56,
    "ashok":23
}
print(marks["shreya"])

a={"key":"value",
   "shreya":"code",
   "marks":"34",
   "my_list":[1,2,9]
  }

print(a.keys()) #key
print(a.values()) #value
print(a.items()) #item
a.update({"nisha":"399"}) #update
print(a.get("shreya")) #get
print(a)

