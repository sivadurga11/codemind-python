def sd(n):
    t=n
    while n>0:
        r= n%10
        if r==0 or t%r!=0:
            return False
        n= n//10
    return True
m= int(input())
n= int(input())
for i in range(m, n+1):
    if sd(i) == True:
        print(i, end= ' ')