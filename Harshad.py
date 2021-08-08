h=int(input("enter the no."))
i=1
s=h
while i>0:
    h=h%10
    s=s+h
    i=i//10
if s%h==0:
    print(True)
else:
    print(False)
                                                                     




