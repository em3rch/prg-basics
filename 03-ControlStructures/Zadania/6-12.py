n_of_purchased_products = int(input("Number of products purchased: "))
product_price = int(input("Product price: "))
amount_to_pay = 0
discount = 0.25

if n_of_purchased_products < 0:
    print("Error!!!")
    exit(1)
elif n_of_purchased_products > 2:
    new_product_price = product_price - (product_price * discount)
    n_of_purchased_products -= 2
    amount_to_pay = (2 * product_price) + (n_of_purchased_products * new_product_price) 
else:
    amount_to_pay = n_of_purchased_products * product_price

print(f"Amount to pay: {amount_to_pay:.2f}")


