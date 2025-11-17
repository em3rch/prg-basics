###
# Calculates the sum of the digits in a number
#
def sum_digits(number: int) -> int:
    sum = 0
    number_in_string = str(number)
    has_minus = False 

    if number < 0 and number_in_string[0] == '-':
        has_minus = True

    if has_minus:
        for i in number_in_string:
            sum += i
        
    return sum




any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')