#write a py pgm using function to convert celsius to fahrenheit
#formula c/5=(f-32)/9
     #    c=5*(f-32)/9
     
def f_to_c(f):
    return  5*(f-32)/9
f=int(input("Enter temperature in F: "))
print(f_to_c(f))