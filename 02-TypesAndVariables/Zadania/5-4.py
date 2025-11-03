amount = float(input("Enter some amount: "))
vat_rate = 0.23
amount_vat = amount * vat_rate 
print(f"Amount   : {amount:.2f}")
print(f"VAT {int(vat_rate * 100)}%  : {amount_vat:.2f}")
