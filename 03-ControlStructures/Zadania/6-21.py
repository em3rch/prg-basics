source_amount_pln = int(input("Enter the amount in PLN: "))
amount_pln = source_amount_pln

coin_1 = 0
coin_2 = 0
coin_5 = 0

while amount_pln != 0:
    if amount_pln % 5 != amount_pln:
        coin_5 += ((amount_pln - (amount_pln % 5)) // 5)
        amount_pln = amount_pln % 5
    elif amount_pln % 2 != 1:
        coin_2 += ((amount_pln - (amount_pln % 2)) // 2)
        amount_pln = amount_pln % 2
    else:
        coin_1 += 1
        amount_pln -= 1

print(f"The amount of PLN {source_amount_pln} in coins:\n"
      f"5 PLN coins: {coin_5}\n"
      f"2 PLN coins: {coin_2}\n"
      f"1 PLN coins: {coin_1}")    
   
