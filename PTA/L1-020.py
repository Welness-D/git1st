N=int(input())
IDlist=set()
handsomeID=[]
for _ in range(N):
    k=input().split()
    if k[0]!="1":   
        k.pop(0)
        IDlist.update(k)
M=int(input())
friendList=input().split(" ",M)
for i in friendList:
    if i not in IDlist:
        handsomeID.append(i)
        IDlist.add(i)
if not handsomeID:
    print("No one is handsome")
else:
    print(" ".join(handsomeID))