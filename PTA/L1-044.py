N=int(input())
rules={"JianDao":"ChuiZi","Bu":"JianDao","ChuiZi":"Bu"}     #{输：赢}
inlist=[]
while 1:
    a=input()
    if a=="End":
        break
    else:
        inlist.append(a)
output=list(map(lambda x:rules[x],inlist))
if len(output)>N:
    for i in range(N,len(output),N+1):
     output[i]=inlist[i]
print(*output,sep="\n")