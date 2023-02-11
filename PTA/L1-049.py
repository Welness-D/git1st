def arrange(collageNum, teamNum):
    numlist = getNum()
    outputlist = {x: [] for x in range(collageNum)}  # 输出列表
    while 1:  # 每次循环为一个周期，给符合条件的学校添加 1队（10个）编号

        # 创建临时列表，来存储本次本次循环要添加到outputlist中的数据（不需添加的学校用空的“[]”占位）
        templist = [[]*x for x in range(collageNum)]

        # 将编号处理后添加到 临时列表 中
        for _ in range(10):
            for i, v in enumerate(templist):
                if teamNum[i] != 0:
                    if teamNum.count(0) == N-1:
                        # 当第一组就是唯一一组时，就要隔位就坐，此时应将“1 3 5 7 9”加入到templist中。如无此操作则加入的是“2 4 6 8 10”
                        if next(numlist) == 1:
                            v.append(1)
                        else:
                            v.append(next(numlist))
                    else:
                        v.append(next(numlist))

        # 将本次循环的编号赋值到输出列表中
        for i, v in outputlist.items():
            v.append(templist[i]) if templist[i] != [] else 1

        # 处理每个学校还剩几队需要添加编号
        for i, v in enumerate(teamNum):
            teamNum[i] -= 1 if teamNum[i] > 0 else 0

        # 所有队伍均赋编号后结束
        if len(set(teamNum)) == 1 and 0 in set(teamNum):
            return outputlist


def getNum():
    n = 0
    while True:
        n = n+1
        yield n


N = int(input())
teamNum = list(map(int, input().split()))
result = arrange(N, teamNum)
for i, v in result.items():
    print(f"#{i+1}")
    [print(*x) for x in v]
