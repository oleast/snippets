
def secret(x):
    n = len(x)
    y = [0]*n

    for i in range(0, n):
        a = x[0]
        k = 0
        for j in range(1, n):
            if a < x[j]:
                a = x[j]
                k = j
        y[i] = a
        x[k] = -1
    return y

def secret2(x):

    a = 0

    while x > 0:
        b = x % 2
        a = a + 1
        x = (x - b) / 10

    y = a

    return y

def main():
    print(secret([1, 4, 8, 2, 5, 8, 10, 1]))
    print(secret2(12345678))

if __name__ == "__main__":
    main()
