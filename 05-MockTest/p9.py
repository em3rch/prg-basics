def f(sentence):
    counter = 0

    for i in sentence:
        if i in "aeiouy":
            counter += 1
        else:
            continue

    return counter


if __name__ == "__main__":
    print(f("water"))
    print(f("hello world"))