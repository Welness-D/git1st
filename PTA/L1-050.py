def generateList(times,inList):
    outList=[]
    for i in a:
        for j in inList:
            outList.append(i+j)
    times-=1
    if times==1:
        return outList
    return generateList(times,outList)


L,N=list(map(int,input().split()))
a=[chr(i) for i in range(97,123)]
reList=generateList(L,a)
print(reList[-N])