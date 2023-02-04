N = int(input())
stuList = []    #学生列表:[(name,sex)*n]
outputList = []
for _ in range(N):
    sex, name = input().split()
    stuList.append((name, sex))
#   生成倒序的学生列表
reverseStuList = list(reversed(stuList))
#   遍历将前半部分的学生，给他配对
for name, sex in stuList[:int(len(stuList)/2)]:
    #在倒序列表按顺序找到第一个符合条件的学生，与当前学生配对
    for i in reverseStuList:
        if sex != i[1]:
            outputList.append((name, i[0]))
            reverseStuList.remove(i)
            break
print("\n".join(map(" ".join, outputList)))
