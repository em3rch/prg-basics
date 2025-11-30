for i in range(1, 8):
    print(i, end=' ')
    mid = i + 7
    for j in range(6):
        print(mid, end=' ') 
        mid = mid + 7

    print()