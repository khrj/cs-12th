def factorial(num):
    if num == 0 or num == 1:
        return 1

    return num * factorial(num - 1)


def nPr(n, r):
    return factorial(n) / factorial(n - r)


def nCr(n, r):
    return factorial(n) / (factorial(n - r) * factorial(r))


n, r = [int(x) for x in input("nPr: input n and r split by commas: ").split(",")]

print(nPr(n, r))

n, r = [int(x) for x in input("nCr: input n and r split by commas: ").split(",")]

print(nCr(n, r))
