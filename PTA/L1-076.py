N,M = list(map(int, input().split()))
priceList=[]
for _ in range(N):
    priceList.append(float(input()))
    
for i in priceList:
    if i<M:
        print("On Sale! %.1f" % i)