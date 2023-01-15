import math #导入数学计算相关的包
maxLen = 0 #最长连续因子个数
resultList = []#连续因子
isPrimary = True #标识是否为质数

num = int(input())

for i in range(2,int(math.sqrt(num))+1):#从2开始依次遍历至最大因子
    tempNum = num
    tempList=[]
    start = i
    while tempNum%start==0:#一轮遍历
        isPrimary=False
        tempNum = tempNum//start
        tempList.append(str(start))
        start+=1
    tempLen=start-i
    if tempLen > maxLen :#更新数据
        resultList=tempList
        maxLen=tempLen

if isPrimary == True:#输出结果
    print(1)
    print(num)
else:
    print(maxLen)
    print("*".join(resultList))