arr=[1,2,3,4,5,6,7,8,9,0]
# cnt=0
found=False
# n=int(input("Enter the number to be searched:"))
n=int(input("Enter the number to be searched:"))
for i in range(len(arr)):
        if(arr[i]==n):
                print("element found at index :",i)
                found=True
                break
if not found:
                print("element not found ")
               


