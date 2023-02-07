N=int(input())
breathe=list(range(15,21))
pulse=list(range(50,71))
inputlist=[]
for _ in range(N):
    a=input().split()
    a=a[:1]+list(map(int,a[1:]))
    inputlist.append(a)
outputlist=[]
for i in inputlist:
    if i[1] in breathe and i[2] in pulse:
        continue
    outputlist.append(i[0])
print(*outputlist,sep="\n")