import math

def diag_perimetru(l):
    diag = l * math.sqrt(2)
    perimetru = 4 * l;

    return [diag, perimetru]
if __name__ == '__main__':
    n = int(input().strip())
    lista = diag_perimetru(n)
    print("diagonala =", lista[0])
    print("perimetru =", lista[1])
