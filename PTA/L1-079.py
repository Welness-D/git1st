
N=int(input())
skillList=list(map(int, input().split()))
print(min(skillList),skillList.count(min(skillList)))
print(max(skillList),skillList.count(max(skillList)))
