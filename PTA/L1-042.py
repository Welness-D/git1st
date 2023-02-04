datelist = input().split("-")
datelist.insert(0,datelist[-1])
datelist.pop()
print("-".join(datelist))