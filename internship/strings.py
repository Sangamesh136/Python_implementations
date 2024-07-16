# n = 0
# c = ''
# r = " "

# for i in range(len(ip)):
#     if i%2 != 0:
#         n = int(ip[i])
#         r+=c*n
#     else:
#         c=ip[i]
# print(r)

# ip = str(input())
# v = ""
# c = ""
# for i in range(0, len(ip)):
#     if ip[i] in 'aeiou':
#         v=v+ip[i]
#     else:
#         c=c+ip[i]
# print(c)
# print(v)


# n = "qwerty"
# print(n[-6:0:-1])

# Unique subsequence(String)
# def ss(s):
#     count=0
#     res=" "
#     for i in range(len(s)):
#         for j in range(i+1,len(s)+1):
#             count=count+1
#             res = res+s[i:j]
#             print(res)
#             res=" "
#     print(count)

# ss("flok")


# def Occurance(s):
#     count=0
#     for i in range(len(s)):
#         if(s[i]=='a'):
#             count+=1
#     return count
# print(Occurance("aaaa"))

def printX(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if i==j or j== len(s)-i-1:
                print(s[i], end=" ")
            else:
                print(" ",end=" ")
        print()

printX("abcdefghi")