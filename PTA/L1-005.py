N=int(input())
stuInf={}
for i in range(N):
    a=input().split()
    stuInf[a[1]]=a[0]+' '+a[2]
M=int(input())
exList=input().split()
for i in exList:
    print(stuInf[i])