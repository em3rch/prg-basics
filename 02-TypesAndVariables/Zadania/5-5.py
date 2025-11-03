product_price = float(input("Enter the product price: "))
discount_percentage = float(input("Enter the discount percentage: "))
price_with_discount = product_price - (product_price * discount_percentage / 100)
reduction = product_price - price_with_discount

print(f"Enter price: {product_price:.2f}")
print(f"Enter discount %: {discount_percentage:.2f}")
print(f"Price with discount: {price_with_discount:.2f}")
print(f"Reduction: {reduction:.2f}")
