current_price = float(input("Enter current product price: "))
previous_price = float(input("Enter previous product price: "))

current_price_percentage_based_on_previous = current_price * 100 / previous_price

if current_price_percentage_based_on_previous <= 90:
    print("But the product!!!")
    print(f"Product price reduced by {int(100 - current_price_percentage_based_on_previous)}%")
