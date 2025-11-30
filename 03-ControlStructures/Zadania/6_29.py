n = int(input("Enter your number: "))

prime_counter = 0
i = 2
while prime_counter != n:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_counter += 1
        print(i, end=' ')
    
    i += 1

print()