W, H = list(map(float, input().split()))
a = W/(H**2)
print("%.1f" % a)
output = "PANG" if a > 25 else "Hai Xing"
print(output)
