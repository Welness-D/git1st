from functools import reduce


N=int(input())
mod=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
check=['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
IDarr=[]
errorList=[]
for i in range(N):
    IDarr.append(input())
for i in IDarr:
    flag=0
    if str(i)[:-1].isnumeric():
        print(list(map(lambda x,y:x*y,list(map(int,i[:-1])),mod)))
        a=reduce(sum,list(map(lambda x,y:x*y,list(map(int,i[:-1])),mod)))   # 第二个参数应为1个list，是每一位都加权后的结果，共17个数
        print(a)
        for j in range(17):
            flag+=int(str(i)[j])*mod[int(j)]
        if check[flag%11] !=str(i)[-1]:
            errorList.append(i)

       


    else:
        errorList.append(i)
if len(errorList)==0:
    print("All passed")
else:
    for i in errorList:
        print(i)