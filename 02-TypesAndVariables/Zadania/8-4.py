###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
inches = cm / 2.54
feet = inches // 12
remain_inches = inches % 12
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {int(feet)} feet and {remain_inches:.2f} inches')