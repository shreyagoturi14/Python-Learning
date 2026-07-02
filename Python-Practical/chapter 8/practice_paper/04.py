# write a recurcive fun to calculate the sum of first n nutural number.
def sum(n):
    if (n==1):
        return 1
    return sum(n-1)+n
sum=int(input("enter a number: "))
print(sum)