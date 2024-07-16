num = 153
count=0
temp = num
arm=0

while temp!=0:
    count+=1
    temp=int( temp/10)
    
print(count)
temp=num

while temp!=0:
    rem=int(temp%10)
    arm=int(arm+rem**count)
    temp=int(temp/10)

if num==arm:
    print("its an armstrong")
else:
    print("Its not an aramstrong")



    
