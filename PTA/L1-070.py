
senList=[]
while 1:
    a=input()
    if a==".":
        break
    senList.append(a)
print(len(senList))
sum=0   #符合条件的句子个数
for i,v in enumerate(senList):
    if "chi1 huo3 guo1" in v:
        sum+=1
        if sum==1:
            idx=i+1
if sum>0:
    print(idx,sum)
else:
    print("-_-#")