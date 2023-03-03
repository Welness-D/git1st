
inp =  list(map(int, input().split()))
tyreList, lowest, threshold = inp[:4],inp[4],inp[5]

for i, v in enumerate(tyreList):
    pass
if min(tyreList) < lowest or max(tyreList)-min(tyreList) > threshold:
    errorNum = tyreList.index(min(tyreList))
    del tyreList[errorNum]

    if min(tyreList) < lowest or max(tyreList)-min(tyreList) > threshold:
        print("Warning: please check all the tires!")
    else:
        print(f"Warning: please check #{errorNum+1}!")
else:
    print("Normal")
