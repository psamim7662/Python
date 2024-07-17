# 8891
# 8891%10=1,889%10=9....
n = int(input("Enter a number: "))  
sum = 0
original_n = n
num_digits = len(str(n))  # Calculating  number of digits in the number

while n > 0:
    digit = n % 10  # Extract the last digit of n
    sum += digit ** num_digits  
    n //= 10  # Remove the last digit from n

if sum == original_n:
    print(original_n, "is an Armstrong number")
else:
    print(original_n, "is not an Armstrong number")
