age = int(input("Enter your age: "))
age_group = ''

if age < 0 or age > 100:
    print("Error!!!")
    exit(1)
elif age < 13:
    age_group = "child"
elif 13 <= age <= 19:
    age_group = "teen"
elif 20 <= age <= 64:
    age_group = "adult"
elif 65 <= age:
    age_group = "senior"

print(f"You belong to '{age_group}' age group.")

