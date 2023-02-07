import numpy as np
import sys as sys
A=[]
B=[]

Arow, Acolumn = list(map(int,input().split()))
for i in range(Arow):
    A.append(list(map(int,input().split())))

Brow, Bcolumn = list(map(int,input().split()))
for i in range(Brow):
    B.append(list(map(int,input().split())))

if Acolumn==Brow:
    Anumpy=np.asarray(A)
    Bnumpy=np.asarray(B)
    X=np.dot(A,B)
    np.set_printoptions(threshold=sys.maxsize)
    [print(*x) for x in X]
else:
    print(f"Error: {Acolumn} != {Brow}")
