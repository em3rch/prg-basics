def f(binary_number):
    for i in binary_number:
        if i == '1' or i == '0':
            continue
        else:
            return False
    
    return True


if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100"))
    print(f("gjgojlq"))
    print(f("5810512067268723"))
    print(f("101000100110011010100010100110001111"))