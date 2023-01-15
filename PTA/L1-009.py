from fractions import Fraction  
N=int(input())
sum=0
for i in input().split():
    sum+=Fraction(i)
if(int(sum) and sum!=int(sum)):
    print(int(sum),sum-int(sum))
else:
    print(sum)

'''
# old version
if(int(sum)):
    if(sum-int(sum)):   #   |sum|>1 and not Integer
        print(int(sum),sum-int(sum))
    else:               #   sum= Integer
        print(int(sum))
else:
    if(sum):            #   -1<sum<1(except 0)
        print(sum)
    else:               #   sum=0
        print(0)
'''
