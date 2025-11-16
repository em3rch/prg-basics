###
# Program that simulates the operation of an electronic thermometer.
#
temperature = -2
if temperature > 35:
    print("It is extremely hot, for a temperature above 35 degrees.")
elif temperature > 30:
    print("It is hot, for a temperature above 30 degrees.")
elif temperature >= 15:
    print("It is warm, for a temperature of at least 15 degrees.")
elif temperature >= 0:
    print("It is cold, for a temperature of at least 0 degrees.")
else:
    print("Warning, frost, for a temperature below 0 degrees.") 

