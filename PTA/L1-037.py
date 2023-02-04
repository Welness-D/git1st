from decimal import Decimal

A, B = list(map(int, input().split()))
if B == 0:
    result = "Error"
else:
    result = Decimal(A/B).quantize(Decimal("0.00"))
B = "("+str(B)+")" if B < 0 else B
print(r"{}/{}={}".format(A, B, result))

