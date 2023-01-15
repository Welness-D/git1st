import re
exlist=["G","P","L","T"]
def sortWithGen(arr):
    while arr:
        for i in exlist:
            if i in arr:
                arr.remove(i)
                yield i

inputStr=input().upper()
strlist=re.findall('[GPLT]',inputStr)
result=sortWithGen(strlist)
print(''.join(result))