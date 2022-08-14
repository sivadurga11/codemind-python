for i in range(int(input())):
    b= int(input())
    d= 0
    m=1
    while b>0:
        r= b%10
        d= d+(r*m)
        m= m*2
        b= b//10
    print(d)