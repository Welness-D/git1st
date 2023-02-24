N=int(input())
w=["You are lucky!","Wish you good luck."]

arr=[]
for _ in range(N):
    arr.append(input())
for i in arr:
    a=list(map(int,i[:3]))
    b=list(map(int,i[3:]))
    if sum(a)==sum(b):
        print(w[0])
    else:
        print(w[1])