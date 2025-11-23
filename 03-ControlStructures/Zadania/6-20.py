n: int = int(input("Enter decimal num: "))

quotient: int = n
remainder: int = 0
rem_values_lst: list = []

binary_n: int = ""

while quotient != 0:
    remainder = quotient  % 2
    quotient = quotient // 2
    rem_values_lst.append(remainder)

print(rem_values_lst)

for i in rem_values_lst:
    binary_n = str(i) + binary_n

print(F"{n}(10) = {binary_n}(2)")





