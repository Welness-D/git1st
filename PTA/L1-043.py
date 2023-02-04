from decimal import Decimal


def getMinute(a, b):
    a = list(map(int, a.split(":")))
    b = list(map(int, b.split(":")))
    x = (b[0]-a[0])*60+(b[1]-a[1])
    return x


N = int(input())
inlist = []
templist = []
temp = 0
# 每一天的记录保存到templist中（不保存管理员的操作），并将templist全部存入inlist
while 1:
    a = input().split()
    if a[0] != "0":
        templist.append(a)
    else:
        inlist.append(templist)
        templist = []
        temp += 1
    if temp == N:
        break

output = []
templist = []
for day in inlist:
    num = time = 0
    while day:
        a = day.pop(0)
        if a[1] == "S":
            templist.append(a)
        elif a[1] == "E":
            for x in templist:
                if x[0] == a[0]:
                    templist.remove(x)
                    num += 1
                    time += getMinute(x[2], a[2])
    output.append(
        [num, Decimal(time/num).quantize(Decimal("0")) if num != 0 else time])
[print(x[0], x[1]) for x in output]
