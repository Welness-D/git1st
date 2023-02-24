# 读入输入数据
Pa, Pb = map(int, input().split())
votes = list(map(int, input().split()))
if all(votes):
    winner = 'b'
    audience_votes = Pb
    judge_votes = 3
elif sum(votes) == 0:
    winner = 'a'
    audience_votes = Pa
    judge_votes = 3
else:
    winner = 'a' if Pa > Pb else 'b'
    audience_votes = Pa if Pa > Pb else Pb
    judge_votes = 3 - sum(votes) if Pa > Pb else sum(votes)
print(f"The winner is {winner}: {audience_votes} + {judge_votes}")
