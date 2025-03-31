def Euklines(a, b):
    while a != b:
        if a < b:
            b -= a
        else:
            a -= b
    print(a)

def NWD(a, b):
    while b:
        t = b
        b = a % b
        a = t
    print(a)

# NWW(10, 5) = 10
#(10 * 5) / NWW(10, 5) = 50/5 = 10

if __name__ == '__main__':
    a = int(input("Wpisz a: "))
    b = int(input("Wpisz b: "))
    print(Euklines(a, b))
    print(NWD(a, b))
