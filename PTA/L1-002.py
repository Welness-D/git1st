a,b=input().split();
a=int(a)

line=int(((a+1)/2)**0.5)    #行数

for i in range(line):
    for j in range(i):
        print(" ",end="")
    for k in range(2*(line-i)-1):
        print(b,end="")
    print()
for i in range(1,line):
    for j in range(line-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print(b,end="")
    print()
print(a-line**2*2+1)