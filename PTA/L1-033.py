y,n = list(map(int,input().split()))
x=0
for i in range(y,3001):
    i=str(i).zfill(4)
    if n==len(set(i)):
        print(x,i,sep=" ")
        break
    x+=1