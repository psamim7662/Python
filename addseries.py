n=int(input("Enter a value for operation: "))
sum=0

for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    t=i/fact
    sum=sum+t
print("the series is:",n,sum)