def f(palindrom):
    reversed_palindrom = ""

    for i in range(-1, -len(palindrom) - 1, -1):
        reversed_palindrom += palindrom[i]

    if palindrom == reversed_palindrom:
        return True
    else:
        return False
    

if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))