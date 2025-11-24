def f(sentence):
    counter = 0

    for i in sentence:
        counter += ord(i)
    
    if counter % 3 == 0:
        return True
    else:
        return False
    

if __name__ == "__main__":
    print(f("hello world"))
    print(f("university"))
    print(f("student"))