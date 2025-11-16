dog_age_in_human_years = int(input("Enter the dog's age in human years: "))

if dog_age_in_human_years < 0 and dog_age_in_human_years > 150:
    print("Error!!!")
    exit(1)
if dog_age_in_human_years > 2:
    dog_age_in_dog_years = (dog_age_in_human_years - 2) * 4
    dog_age_in_dog_years += 21
elif dog_age_in_human_years == 1:
    dog_age_in_dog_years = 10.5
elif dog_age_in_human_years == 2:
    dog_age_in_dog_years = 21

print(f"The dog's age in dog's years is: {dog_age_in_dog_years}")
