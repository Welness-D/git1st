def running(arrlist):
    pass
x,y,N=list(map(int, input().split()))
arrlist=[x,y]
outputlist=[]
step=0
while 1:
    a=arrlist[step]*arrlist[step+1]
    b=list(map(int,list(str(a))))
    arrlist.extend(b)
    step+=1
    if len(arrlist)>=N:
        print(*arrlist[:N])
        break