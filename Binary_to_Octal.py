for i in range(int(input())):
    def BinToOct(b):
        return oct(int(b,2))
    b= input()
    o= BinToOct(b)
    print(o[2:])