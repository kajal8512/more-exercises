string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 
i=0
k=[]
while i<len(string_list):
    n=string_list[i]
    if n not in k:
        k.append(n)
    i+=1
print(k)


