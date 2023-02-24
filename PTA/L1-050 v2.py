def generateList(times,inList):
    outList=gg(inList)
    times-=1
    if times==1:
        return outList
    return generateList(times,outList)
def gg(inList):
    for i in inList:
        for j in a:
            yield i+j

L,N=list(map(int,input().split()))
a=[chr(i) for i in range(122,96,-1)]
reList=generateList(L,(i for i in a))
for i,v in enumerate(reList):
    if i==N-1:
        print(v)