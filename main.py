#def Euklines(a, b):
#    while a != b:
#        if a < b:
#            b -= a
#        else:
#            a -= b
#    print(a)
from math import floor


#def NWD(a, b):
#    while b:
#        t = b
#        b = a % b
#        a = t
#    print(a)

# NWW(10, 5) = 10
#(10 * 5) / NWW(10, 5) = 50/5 = 10

def numeroUno(n):
    for i in range(2, int(n ** 0,5)+1):
        if n % i == 0:
            return False
    return True



if __name__ == '__main__':
#    a = int(input("Wpisz a: "))
#    b = int(input("Wpisz b: "))
    n = int(input("Wpisz n: "))
#    print(Euklines(a, b))
#    print(NWD(a, b))
