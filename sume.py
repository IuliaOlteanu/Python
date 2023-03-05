def suma(n):
    suma_cifre = 0
    while n > 0:
        suma_cifre = suma_cifre + n % 10
        n = n // 10
    return suma_cifre

if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    for i in range(n, m):
        if i % suma(i) == 0:
            print(i)
