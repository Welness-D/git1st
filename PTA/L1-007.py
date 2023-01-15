pinyinDic={"0": "ling","1": "yi","2": "er","3": "san","4": "si","5": "wu","6": "liu","7": "qi","8": "ba","9": "jiu","-":"fu"}

N=list(input())
a=[]
for i in N:
    a.append(pinyinDic[i])
print(" ".join(a))
for i in N:
    print(pinyinDic[i],end=" ")