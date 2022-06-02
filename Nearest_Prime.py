def prime(n):
    fc=0
    for i in range(1, n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False
def previous_prime(n):
    while prime(n) == False:
        n=n-1
    return n
def next_prime(n):
    while prime(n)== False:
        n=n+1
    return n
def nearest_prime(n):
    a= previous_prime(n)
    b= next_prime(n)
    if n-a<=b-n:
        print(a)
    else:
        print(b)
test= int(input())
for i in range(test):
    x= int(input())
    nearest_prime(x)