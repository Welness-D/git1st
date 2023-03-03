from functools import reduce
N = int(input())
numList = list(map(float, input().split()))
sum = reduce(lambda x, y: x+y, map(lambda x: 1/x, numList))
result=1/(sum/N)
print("%.2f" % result)
