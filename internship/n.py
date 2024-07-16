# num = 153
# count=0
# temp = num
# arm=0

# while temp!=0:
#     count+=1
#     temp=int( temp/10)
    
# print(count)
# temp=num

# while temp!=0:
#     rem=int(temp%10)
#     arm=int(arm+rem**count)
#     temp=int(temp/10)

# if num==arm:
#     print("its an armstrong")
# else:
#     print("Its not an aramstrong")

# def add(a,b):
#     c= a+b
#     return c
# d=add(4,5)
# print(d)
n = int(input("Enter the number:"))
def diamond(n):
    for i in range(1,n+1):
        print(" " * (n-i) + "*"*(2*i-1))
    for i in range(n-1,0,-1):
        print(" "*(n-i)+ "*"*(2*i-1) )

diamond(n)

