person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print(f"Name: {person['name']}")

print(f"Hobby: {person['hobby']}")

print(f"{key} : {value}" for key, value in person.items())

person["surname"] = "Novak"
person["married"] = not person ["married"]
person["gender"] = "male"
person["hobby"] += "bicycle"

new_dict = person["phone"]
new_dict["work"] = "313131444"

person["phone"] = new_dict

for key, value in person.items():
    print(f"{key} : {value}")