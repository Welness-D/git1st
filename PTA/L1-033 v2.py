y,n = list(map(int,input().split()))

    
def caculate(y,x):
    ys=str(y).zfill(4)
    if n==len(set(ys)):
        return ys,x
    return caculate(y+1,x+1)
a,b=caculate(y,0)
print(b,a,sep=" ")