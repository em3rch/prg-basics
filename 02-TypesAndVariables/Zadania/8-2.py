###
# Calculation of circle area and circumference 
#

# determine radius and PI values
r = float(input("Enter radius: "))
pi = 3.14 
# calculate area 
area = pi * r ** 2
# calculate circumference 
circumference = 2 * pi * r
# print results
print(f"Circumference = {circumference:.2f}, area = {area:.2f}")