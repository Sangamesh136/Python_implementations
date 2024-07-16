# def xpattern(n):
#     for i in range(len(n)):
#         for j in range(len(n)):
#             if i==0 or j==n-i-1:
#                 print(n[i], end=" ")
#             else:
#                 print(" ",end=" ")
#         print()


# m=(1,2,3,4,5,6,7,8,9)
# n=[list(m)]
# xpattern(n)

def printX(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if i==j or j== len(s)-i-1:
                print(s[i], end=" ")
            else:
                print(" ",end=" ")
        print()

m=(1,2,3,4,5,6,7,8,9)
n=[list(m)]
printX(m)