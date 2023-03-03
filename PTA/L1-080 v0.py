x,y,N=list(map(int, input().split()))
arrlist=[x,y]
outputlist=[]
while 1:
    a=arrlist[0]*arrlist[1]
    a=list(map(int,list(str(a))))
    arrlist.extend(a)
    b=arrlist.pop(0)
    outputlist.append(b)
    if len(outputlist)==N:
        break
print(*outputlist)