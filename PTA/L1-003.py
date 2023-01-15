
N=input();
N=list(N)
dictN={}
for i in N:
    dictN[i]=dictN.get(i,0)+1
listN=list(dictN.items())
listN.sort()

for k,v in listN:
    print(k,":",v)