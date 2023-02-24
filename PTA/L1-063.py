N = int(input())
prompt = ["duo chi yu!", "duo chi rou!",
          "wan mei!", "ni li hai!", "shao chi rou!"]
standard = [[129, 25], [130, 27]]
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))
for i in arr:
    a = i[0]
    if i[1] > standard[a][0]:
        print(prompt[3],end=" ")
    elif i[1] < standard[a][0]:
        print(prompt[0],end=" ")
    else:
        print(prompt[2],end=" ")
        
    if i[2] > standard[a][1]:
        print(prompt[4])
    elif i[2] < standard[a][1]:
        print(prompt[1])
    else:
        print(prompt[2])
