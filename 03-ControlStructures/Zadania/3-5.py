###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12): '))

if month % 2 != 0:
    days = 31 ## months with 31 days
elif month == 2:
    days = 28
elif month % 2 == 0:
    days = 30

print(f'Month {month} has {days} days')