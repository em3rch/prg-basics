i = 6
while True:
    j = 1
    while j != 4:
        print(f"{i + j}", end=' ')
        j += 1

    print()

    i -= 3

    if i < 0:
        break
        
print()
