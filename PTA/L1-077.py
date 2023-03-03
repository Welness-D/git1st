feelings=list(map(int, input().split()))
hours=[x for x in range(24)]
while 1:
    a = int(input())
    if a not in hours:
        break
    x="Yes" if feelings[a]>50 else "No"
    print(feelings[a],x,sep=" ")