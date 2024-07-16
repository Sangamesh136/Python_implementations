
# tailed recursion:
# def recurFun(n):
#     if(n>=0):
#         print(n)
#     return recurFun(n-1)

# n=95
# recurFun(n)

# Head Recursion:

# def recurFun(n):
#     if(n>0):
#         recurFun(n-1)
#         print(n, end= " ")

# recurFun(30)


# def f(n):
#     if(n>0):
#         res = n+ f(n-3)
#         print(res)
#     else:
#         res = 0
#     return res

# f(12)

def f(n):
    if(n>0):
        res = n+ f(n-3)+ f(n-6)
        print(res)
    else:
        res = 0
    return res

f(9)