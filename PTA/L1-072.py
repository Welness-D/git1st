
price = {0: 0, 6: 10000, 7: 36, 8: 720, 9: 360, 10: 80, 11: 252, 12: 108, 13: 72, 14: 54,
         15: 180, 16: 72, 17: 180, 18: 119, 19: 36, 20: 306, 21: 1080, 22: 144, 23: 1800, 24: 3600}
standard = {1: [0, 1, 2], 2: [3, 4, 5], 3: [6, 7, 8], 4: [
    0, 3, 6], 5: [1, 4, 7], 6: [2, 5, 8], 7: [0, 4, 8], 8: [2, 4, 6]}
# 彩票数字排列
lottery = []
# 刮开数字的idx
goalsidx = []
# 1-3行输入
for _ in range(3):
    lottery.extend(list(map(int, input().split())))
# 4-6行输入
for _ in range(3):
    x, y = list(map(int, input().split()))
    a = 3*(x-1)+(y-1)
    goalsidx.append(a)
# 7行输入
choose = int(input())
# 输出刮开的数字
for i in goalsidx:
    print(lottery[i])
# 处理彩票，将0更换为对应的数字
zeroidx = lottery.index(0)
for i in range(1, 10):
    if i not in lottery:
        lottery[zeroidx] = i

sum = 0
for i in standard[choose]:
    sum += lottery[i]
print(price[sum])
