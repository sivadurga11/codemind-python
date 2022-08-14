m,n = map(int,input().split())
a= list(map(int,input().split()))
b= list(map(int,input().split()))
c= 0
for i in b:
    if i in a:
        c+=1
        k= a.index(i)
        a.pop(k)
print('Yes' if c==len(b) else'No')