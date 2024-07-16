num = 9
numSqr = num**2
sum=0
temp=numSqr
while numSqr!=0:
    rem=int(numSqr%10)
    sum=int(sum+rem)
    numSqr=int(numSqr/10)

if(sum==num):
    print("yes")
else:
    print("no")
    