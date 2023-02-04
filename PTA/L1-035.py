namelist=[]
while 1:
    a=input()
    if a==".":
        break
    namelist.append(a)
L=len(namelist)
if L>14:
    print("{} and {} are inviting you to dinner...".format(namelist[1],namelist[13]))
elif 2<=L<14:
    print("{} is the only one for you...".format(namelist[1]))
elif L<2:
    print("Momo... No one is for you ...")    