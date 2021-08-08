'''list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
i=0
k=[]
while i<len(list1):
    n=list1[i]
    if n not in k:
        k.append(n)
    i+=1
j=0
while j<len(list2):
    m=list2[j]
    if m not in k:
        k.append(m)
        k.sort()
    j+=1
print(k)'''
