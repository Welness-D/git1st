inputdate=input()
if len(inputdate)==6:
    print("-".join([inputdate[:4],inputdate[4:]]))
else:
    if int(inputdate[:2])<22:
        print("20"+"-".join([inputdate[:2],inputdate[2:]]))
    else:
        print("19"+"-".join([inputdate[:2],inputdate[2:]]))