L,N=list(map(int,input().split()))
a=[chr(i) for i in range(122,96,-1)]
output=[]
N=N-1
for i in range(L):
    x=N%26
    output.insert(0,a[x])
    N=int(N/26)
print("".join(output))