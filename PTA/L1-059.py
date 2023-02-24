import re

N=int(input())
poetryList=[]
for _ in range(N):
    poetryList.append(input())

for i in poetryList:
    a=re.search(r".*(ong), .*(ong)\.",i)
    if a:
        poetry = re.sub(r"([a-z]+) ([a-z]+) ([a-z]+)\.$", "qiao ben zhong.", i)
        print(poetry)
    else:
        print("Skipped")