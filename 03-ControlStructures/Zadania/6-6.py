hours_of_parking = int(input("Enter hours of parking: "))

if 1 <= hours_of_parking <= 2:
    fee = 5
elif 3 <= hours_of_parking <= 6:
    fee = 15
elif 6 < hours_of_parking:
    fee = 20

print(f"For {hours_of_parking} h, your fee will be {fee}.")