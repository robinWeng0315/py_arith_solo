# 1..n累加和
def add(n):
    i = 0
    sum = 0
    while i <= n:
        sum = sum + i
        i += 1

    print(sum)


if __name__ == '__main__':
    add(5)
