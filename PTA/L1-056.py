N = int(input())
namelist = []
numlist = []
for _ in range(N):
    a = input().split()
    namelist.append(a[0])
    numlist.append(int(a[1]))

sum = 0
for i in numlist:
    sum += i
halfAverage = int(sum/N/2)

alist = list(map(lambda x: abs(x-halfAverage), numlist))
winnerIndex = alist.index(min(alist))
print(halfAverage, namelist[winnerIndex])
