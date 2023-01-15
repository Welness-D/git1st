# N=int(input())
# S=0
# for i in range(1,N+1):
#     x=1
#     for j in range(1,i+1):
#         x*=j
#     S+=x
# print(S)


# from functools import reduce
# def getFactorial(n):
#     return reduce(lambda x,y:x*y,range(1,n+1))
# N = int(input())
# S=reduce(lambda x, y: x+y, map(getFactorial, range(1, N+1)))
# print(S)


# from functools import reduce
# N = int(input())
# S = 0
# for i in range(1, N+1):
#     S += factorial(i)
# print(S)


from functools import reduce
from math import factorial
N = int(input())
print(reduce(lambda x, y: x+y, map(factorial,range(1,N+1))))
