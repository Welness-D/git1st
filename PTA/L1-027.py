num=input()
arr=list(set(num))
arr.sort(reverse=True)
index=[]
for i in list(num):
    index.append(str(arr.index(i)))
print(r"int[] arr = new int[]{{{}}};".format(",".join(arr)))
print(r"int[] index = new int[]{{{}}};".format(",".join(index)))