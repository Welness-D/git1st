from functools import reduce


def transpose(arr, column):
    output = [[] for x in range(column)]
    for i in arr:
        for x in range(column):
            output[x].append(i[x])
    return output


A = []
B = []
Arow, Acolumn = list(map(int, input().split()))
for i in range(Arow):
    A.append(list(map(int, input().split())))

Brow, Bcolumn = list(map(int, input().split()))
for i in range(Brow):
    B.append(list(map(int, input().split())))

output = []
if Acolumn == Brow:
    Btrans = transpose(B, Bcolumn)
    for a in A:
        out = []
        for b in Btrans:
            x = reduce(lambda x, y: x+y, map(lambda x, y: x*y, a, b))
            out.append(x)
        output.append(out)
    print(Arow, Bcolumn)
    [print(*x) for x in output]
else:
    print(f"Error: {Acolumn} != {Brow}")
