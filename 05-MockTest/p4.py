def f(card_number):
    return card_number[0] + card_number[1] + ('*' * 10) + card_number[-4:]


if __name__ == "__main__":
    print(f("5290345678909022"))
    print(f("6990345678901388"))