x = int(input("Enter x: "))
y = int(input("Enter y: "))

const_message = f"Point P({x},{y}) "
special_cases = False
if x == 0 and y == 0:
    special_cases = True
    message = const_message + "is located in the central position of the coordinate system."
elif x == 0 and (y < 0 or y > 0):
    special_cases = True
    message = const_message + "is located on Y-axis"
elif y == 0 and (x < 0 or x > 0):
    special_cases = True
    message = const_message + "is located on X-axis"
elif x > 0 and y > 0:
    quad = "first"
elif x < 0 and y > 0:
    quad = "second"
elif x < 0 and y < 0:
    quad = "third"
else:
    quad = "forth"


if not special_cases:
    message = const_message + f"is in the {quad} quadrant of the coordinate system."


print(message)

