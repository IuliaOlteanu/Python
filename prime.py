def prim(n):
    flag = 0
    if n > 1:
        for d in range(2, int(n / 2) + 1):
            if n % d == 0:
                flag = 1
                break
    return flag


if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())

    for i in range(n, m):
        if prim(i) == 0:
            print(i)
