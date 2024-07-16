num = 121
rev = 0
temp = num
count = 0
# while temp!=0:
#     temp=temp%10;
#     count+=1;
    

    
while temp!=0:
    rem=int(temp%10)
    rev=int(rev*10+rem)
    temp=int(temp/10)

if rev==num:
    print("it is palindrome")
else:
    print("its not a palindrome")