N=int(input())
arr=input().split(" ",N)
arr=list(map(int,arr))
odd=[]
even=[]
for i in arr:
    if i%2==1:
        odd.append(i)
print("{} {}".format(len(odd),len(arr)-len(odd)))

