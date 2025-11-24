###
# Calculates the sum of the digits in a number
#
def sum_digits(number: str) -> int:
    if number[1:].isdigit():
        has_minus = False 
        number_in_str: str = str(number)
        sum = 0

        int_number = int(number)

        if int_number < 0:
            number_in_str: str = str(abs())
            has_minus = True
        elif number == 0:
            return 0

        for i in number_in_str:
            sum += int(i)

        if has_minus:
            sum = -sum

        return sum
    else:
        print("Error")
        exit(1)

any_number = input('Enter integer number: ')
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')