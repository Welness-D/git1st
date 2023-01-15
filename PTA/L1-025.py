A, B = input().split(" ", 1)
A = A if A.isdecimal() and 1<=int(A)<=1000 else "?"
B = B if B.isdecimal() and 1<=int(B)<=1000 else "?"
C = int(A)+int(B) if A.isdecimal() and B.isdecimal() else "?"
print(r"{} + {} = {}".format(A, B, C))
