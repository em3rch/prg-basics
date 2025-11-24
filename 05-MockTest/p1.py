def f(amount_to_pay: int) -> int:
    coins_5 = 0
    coins_2 = 0
    coins_1 = 0

    while amount_to_pay != 0:
        if (amount_to_pay % 5) != amount_to_pay:

            coins_5 += ((amount_to_pay - (amount_to_pay % 5)) // 5)
            amount_to_pay = amount_to_pay % 5

        elif amount_to_pay % 2 != amount_to_pay:
            coins_2 += ((amount_to_pay - (amount_to_pay % 2)) // 2)
            amount_to_pay = amount_to_pay % 2
        elif amount_to_pay == 1:
            coins_1 += 1
            amount_to_pay = 0
    
    return coins_5 + coins_2 + coins_1



if __name__ == "__main__":
    print(f(18))
    print(f(23))
    print(f(8))