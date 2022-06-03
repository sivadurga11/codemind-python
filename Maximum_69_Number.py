n= int(input())
n= str(n)
n= list(n)
for i in range(0,len(n)):
    if n[i]=="6":
        n[i]='9'
        break
n=''.join(n)
print(n)