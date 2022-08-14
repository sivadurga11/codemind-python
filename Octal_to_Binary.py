for i in range(int(input())):
    def OctToBin(o):
        return bin(int(o,8))
    o= input()
    b= OctToBin(o)
    print(b[2:])