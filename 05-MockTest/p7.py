def f(n):
    current = 1
    previous = 0
    mid = 0
    for i in range(n - 2):
        mid = current
        current = current + previous
        previous = mid
        

    return current


if __name__ == "__main__":
    print(f(5))
    print(f(9))
    print(f(12))