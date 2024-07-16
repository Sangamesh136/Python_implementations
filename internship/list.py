# d=[1,2,2.5,'a',"Name"]
# # print(type(d))
# print(d)
# d.append(11)
# print(d)
# d.insert(3, 45)
# print(d)

# print(d.pop())
# print(d)
# d.remove('a')
# print(d)


# def swap(a,b):
#     a=a+b
#     b=a-b
#     a=a-b
# def rev(l):
#     j=len(l) - 1
#     i=0
#     # for i in range(len(l)):
#     #     if(l[i]<=l[j]): #No need to check this !
#     #         # swap(l[i],l[j])
#     #         temp = l[i]
#     #         l[i]=l[j]
#     #         l[j]=temp
#     #         # j-=1
#     #     j-=1 
#     #     i+=1
#     #     if(j<=i):
#     #         break
#     #     #break the loop when i and j meet or i > j

#     while(i<=j):
#         if(i<=j):
#             l[i]=l[i]+l[j]
#             l[j]=l[i]-l[j]
#             l[i]=l[i]-l[j]
#         j-=1
#         i+=1
#     return l

#     # return l    
# # size = int(input("Enter the size of the list"))
# # for i in range(size+1):
# #     l= [i]
# l=[10,2,30,4,50,6]
# # rev(l)
# print(rev(l))


li = [1,2,3,4,5]
n=3
newli=[]
j=0
for i in range(len(li)-3,len(li)):
    newli[j]=li[i]
