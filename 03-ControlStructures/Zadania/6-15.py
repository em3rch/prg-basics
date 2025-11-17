ean_13_number = input("Enter EAN-13 article number: ")

if ean_13_number.isdigit() and len(ean_13_number) == 13:
    print("Article number is correct.")

    if ean_13_number[0:3] == "590":
        print("Article manufactured in Poland.")
    else:
        print("Article manufactured elsewhere.")
else:
    print("Article number IS NOT correct.")
    