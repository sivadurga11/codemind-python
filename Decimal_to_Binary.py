for _ in range(int(input())):
    d= int(input())
    b= 0
    m=1
    while d>0:
        t= d%2
        b= b+(t*m)
        m= m*10
        d= d//2
    print(b)