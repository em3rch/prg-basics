previous = 0
current = 1
medium = 0

print(previous, current, end=' ')

for i in range(22):
    medium = current
    current = current + previous
    previous = medium

    print(current, end=' ') 

print()