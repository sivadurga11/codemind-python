def add(n):
    s= 0
    while n>0:
        r= n%10
        s= s+r
        n= n//10
    return s
z= int(input())
while z>9:
    z= add(z)
print(z)
        