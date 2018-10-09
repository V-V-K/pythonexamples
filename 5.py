#Armstrong number check upto 3 digits only
origNum = int(input("Enter a positive  integer: "))
num = origNum;
sum=0
while(num != 0):
    rem = num % 10
    sum += rem ** 3
    num //= 10

if(sum == origNum):
    print(origNum," is an Armstrong number.")
else:
    print(origNum," is not an Armstrong number.")
