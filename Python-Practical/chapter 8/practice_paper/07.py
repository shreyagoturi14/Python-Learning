#write py fun to remove a given word from a list and strip it at the same
def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["shaeya","hem","asha","nisha"]
print(rem(l,"sh"))
