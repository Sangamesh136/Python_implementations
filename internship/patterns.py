# for i in range(1,4):
#     for j in range(1,4):
#         print("*", end = " ")
#     print()
    
# for i in range(3):
    # for j in range(i+1):
    #     print("*", end = " ")
    # print()
    
# n = int(input("Enter the number"))
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==n-1 or i==j:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = int(input("Enter the number"))
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==n-1 or j==n-1 or i==0:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==0 or j==n-i-1:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()

n = 5
for i in range(n):
    for j in range(n):
        if i==j or j==n-i-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

# n = 5
# for i in range(n):
#     for j in range(n-i-1):
#         print("*",end=" ");
#     # for k in range()
#     # print()
    
# n = 5
# for i in range(1,n+1):
#     print(" " * (n-i) + "*"*(2*i-1))
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+ "*"*(2*i-1) )
    





