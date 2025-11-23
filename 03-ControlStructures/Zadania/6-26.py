actual_pin = "0805"

for i in range(3):
    pin_enter = input("Enter the PIN code: ")

    if pin_enter == actual_pin:
        break
    else:
        print("Incorrect...")
else:
    print("Sorry, your payment card has been blocked.")
