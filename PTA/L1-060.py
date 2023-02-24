x,y= list(map(int, input().split()))
a=100*100/2-100*(100-x)/2-100*y/2
a=100*(x-y)/2
print(int(a))