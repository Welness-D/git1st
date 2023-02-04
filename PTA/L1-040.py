from decimal import Decimal
N = int(input())
userlist=[]
for _ in range(N):
    userlist.append(input().split())
output=[]
for i in userlist:
    if i[0]=="M":
        a=Decimal(float(i[1])/1.09).quantize(Decimal("0.00"))
    else:
        a=Decimal(float(i[1])*1.09).quantize(Decimal("0.00"))
    output.append(a)
    
        
[print(x) for x in output]