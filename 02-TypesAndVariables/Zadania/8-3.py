###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celsius_temp = float(input("Enter temperature in Celsius: "))

print(f"Temperature in Kelvin: {celsius_temp + 273.15}")
print(f"Temperature in Fahrenheit: {celsius_temp * (9 / 5) + 32}")
