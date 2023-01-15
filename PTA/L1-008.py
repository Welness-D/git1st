a, b = list(map(int, input().split()))
numlist = list(range(a, b+1))
for i in range(0,len(numlist),5):
    nlist=numlist[i:i+5]
    for i in nlist:
        print(repr(i).rjust(5), end='')
    print()
sum(numlist)
print("Sum = {}".format(sum(numlist)))