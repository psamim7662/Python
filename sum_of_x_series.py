# sign=-1 to multiply with next term 
# initializes=3,updation=2 bcz of factorial difference is 2,condition=limit
# degree(x)=redian=x*3.14/180
n=int(input("Enter the first number: "))
x=float(input("Enter the second number:"))
sum=x
x=x*3.14/180
p=1
f=1
sign=-1
for i in range(3,n+1,2):
    x=x*sign
    p=pow(x,i)
    f=f+i*(i-1)#5!=5*4*3!
    sum=sum+p/f
print(sum)