N=int(input())
blogList=[]
blogD={}
for _ in range(N):
    Flist=input().split()
    Flist.pop(0)
    blogList+=Flist
for i in set(blogList):
    blogD[i]=blogList.count(i)


#方案1    
r=list(blogD.items())
r.sort(key=lambda x:(x[1],x[0]),reverse=False)
a=list(map(str,r[-1]))
print(" ".join(a))

# 方案2
result=max(zip(blogD.values(),blogD.keys()))
print(result[1],result[0],sep=" ")
