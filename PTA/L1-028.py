import math
def isPrime(num):
    if num==1:
        return "No"
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return "No"
    return "Yes"

N=int(input())
arrlist=[]
for i in range(N):
    arrlist.append(int(input()))
resultlist=list(map(isPrime,arrlist))
print(*resultlist,sep="\n")
