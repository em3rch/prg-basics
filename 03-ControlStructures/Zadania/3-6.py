###
# Checks if the given day number of the month is correct
#
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_ok = False

if month % 2 != 0:
    if 1 <= day <= 31:
        day_ok = True
elif month == 2:
    if 1 <= day <= 28:
        day_ok = True
elif month % 2 == 0:
    if 1 <= day <= 30:
        day_ok = True
else:
    day_ok = False

message = f'Day {day} for the month {month}'
if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} IS NOT correct!!!')