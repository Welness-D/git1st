import re
exlist=["G","P","L","T"]

def mysort(arr):
    outputarr=[]
    return sortByExlist(arr,outputarr)

def sortByExlist(arr,output):
    if not arr:
        return output
    for i in exlist:
        if i in arr:
            arr.remove(i)
            output.append(i)
    return sortByExlist(arr,output)

inputStr=input().upper()
strlist=re.findall('[GPLT]',inputStr)
result=mysort(strlist)
print("".join(result))