import re

def SortByGPLT(strlist):
    a=["G","P","L","T"]
    output=[]
    
    strlist.index("G")
    
    L=iter(strlist)
    while True:
        try:
            x = next(L)
            
        except StopIteration:
            # 遇到StopIteration就退出循环
            break

aaa=input().upper()
strlist=re.findall('[GPLT]',aaa)

print(''.join(strlist))

list(map(SortByGPLT,strlist))