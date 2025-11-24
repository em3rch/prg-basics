def f(name):
    name_lst: list = name.split()
    result_str: str = ""

    for i in name_lst:
        if i[0].isalpha():
            result_str += i[0]
        else:
            continue
    
    return result_str


if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))
    print(f("  Exactl Int"))
    print(f(". is my Line: :"))
    print(f("For Your Information"))