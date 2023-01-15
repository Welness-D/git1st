A = "I Love GPLT"
#(1)
for i in list(A):
    print(i)
#(2)
print(*A, sep="\n")
#(3)
[print(i) for i in list(A)]
