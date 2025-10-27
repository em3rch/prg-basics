import math

height = float(input("Provide your height in meters: "))
distance_to_horizon = 3.57 * math.sqrt(height)

print("Distance to the horizon from the point where you stand is ", distance_to_horizon, " km")
