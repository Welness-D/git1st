proparr=[2.455,1.26]
density,prop,distance=input().split()
density=float(density)
prop=int(prop)
distance=float(distance)
a=density*proparr[prop]
result=a/distance
print("%.2f" % a,end=" ")
print("T_T") if result>1 else print("^_^")