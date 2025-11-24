def f(number, even):
    has_minus = False
    result_sum = 0

    if number < 0:
        has_minus = True
        number = abs(number)


    if even == True:
        for i in str(number):
            if int(i) % 2 == 0:
                result_sum += int(i)
            else:
                continue
    elif even == False:
        for i in str(number):
            if int(i) % 2 != 0:
                result_sum += int(i)
            else:
                continue


    if has_minus:
        result_sum = -result_sum

    return result_sum


if __name__ == "__main__":
    print(f(3124, True))
    print(f(3124, False))
    print(f(20576, False))
    print(f(20576, True))
    print(f(13115, True))
    print(f(268, False))
    print(f(-3124, True))
