import math

###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
def triangle_area(a: int, b: int, c: int) -> float:
    p = (a + b + c) / 2

    return math.sqrt(p * (p - a) * (p - b) * (p - c))

a, b, c = map(int, input("Enter 3 sides separated by space: ").split())

print(f"The area of a triangle with sides a = {a}, b = {b}, c = {c} is {int(triangle_area(a, b, c))}")
