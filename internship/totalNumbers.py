# num=int(input("Enter the value of the element:"))
# num = 1234
# count =0
# while num!=0:
#     rem=num%10
#     count +=1
#     num = int(num/10)
    
# print(count)

num=12223334
digit = 2
count=0
while num!=0:
    rem=num%10
    if rem==digit:
        count+=1
    num=int(num/10)
print(count)