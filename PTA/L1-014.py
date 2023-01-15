from decimal import *
# N,c=input().split()
# N=int(N)
# for i in range(round(N/2)):
#     print(c*N)
N=int(input())
print(Decimal(str(N/2)).quantize(Decimal('0')))
