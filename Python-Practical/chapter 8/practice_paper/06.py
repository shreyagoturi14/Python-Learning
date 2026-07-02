#write a python fun which converts inches to cms.

def inch_to_cms(inch):
    return  inch*2.54
n=int(input("Enter in inches: "))
print(f"the corresponding value in cms os {inch_to_cms(n)}")