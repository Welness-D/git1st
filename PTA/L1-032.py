N, s = input().split()
N = int(N)
inputstr = input()
if len(inputstr) > N:
    print(inputstr[-N:])
else:
    print(inputstr.rjust(N, s))
