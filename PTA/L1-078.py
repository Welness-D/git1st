N, M = list(map(int, input().split()))
topicList = []
for _ in range(N):
    topicList.append(input())
for i in topicList:
    
    if i.find("qiandao") != -1 or i.find("easy") != -1:
        continue
    M -= 1
    if M < 0:
        print(i)
        break
if M >= 0:
    print("Wo AK le")
