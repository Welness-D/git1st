x=int(input())
y=1
while 1:
    if y%x==0:
        s=y//x
        n=len(str(y))
        break  
    y=y*10+1
print(s,n)