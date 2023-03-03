N, M = list(map(int, input().split()))

answerList = []
for _ in range(M):
    answerList.append(input())
for answer in answerList:
    NuN = 1
    for i, v in enumerate(answer):
        if v == "y":
            pass
        else:
            NuN += 2**(N-i-1)
    print(NuN)
