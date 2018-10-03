#!/usr/bin/python3

def task_a(k):
    x1 = 0
    x2 = 1
    x3 = x1 + x2
    for x in range(4, k + 1):
        if x % 3 == 0:
            x3 = x1 + x2
        elif x % 3 == 1:
            x1 = x2 + x3
        else:
            x2 = x1 + x3

    return max(x1, x2, x3)

def task_b(k):
    x1 = 0
    x2 = 1
    x3 = x1 + x2
    s = x1 + x2 + x3
    for x in range(4, k + 1):
        if x % 3 == 0:
            x3 = x1 + x2
            s += x3
        elif x % 3 == 1:
            x1 = x2 + x3
            s += x1
        else:
            x2 = x1 + x3
            s += x2

    return max(x1, x2, x3), s

def task_c(k):
    x1 = 0
    x2 = 1
    x3 = x1 + x2
    s = x1 + x2 + x3
    l = [x1, x2, x3]
    for x in range(4, k + 1):
        if x % 3 == 0:
            x3 = x1 + x2
            s += x3
            l.append(x3)
        elif x % 3 == 1:
            x1 = x2 + x3
            s += x1
            l.append(x1)
        else:
            x2 = x1 + x3
            s += x2
            l.append(x2)

    return max(x1, x2, x3), s, l

if __name__ == "__main__":
    print(task_a(10))
    print(task_b(10)[1])
    print(task_c(10)[2])

