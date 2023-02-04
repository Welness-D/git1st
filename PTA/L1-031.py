N = int(input())
peopleList = []    #学生列表:[(name,sex)*n]
for _ in range(N):
    H, W = map(int,input().split())
    peopleList.append((H, W))
for H,W in peopleList:
    WW=(H-100)*0.9
    if abs(W/2-WW)<WW*0.1:
        print("You are wan mei!")
    elif W/2-WW>0:
        print("You are tai pang le!")
    elif W/2-WW<0:
        print("You are tai shou le!")