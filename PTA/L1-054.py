def isPerfect(arr):
    for i in range(N):
        if arr[i][::-1] != arr[-1-i]:
            return False
    print("bu yong dao le")
    [print(*x, sep="") for x in arr]
    return True


symbol, N = input().split()
N = int(N)
inList = []
for _ in range(N):
    inList.append(input().strip())
for row_i, row_v in enumerate(inList):
    for i, v in enumerate(row_v):
        if v == "@":
         row_v[i] = symbol if v == "@" else True

if not isPerfect(inList):
    outputList = []
    for i in range(N):
        outputList.append(inList[i][::-1])
    outputList.reverse()
    [print(*x, sep="") for x in outputList]
