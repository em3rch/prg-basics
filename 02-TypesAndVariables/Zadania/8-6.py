###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption in liters per 100km: '))
total_fuel_consumption = distance / 100 * fuel_consumption 
total_cost = fuel_price * total_fuel_consumption 
print(f'The total fuel consumption in liters on the given distance is: {total_fuel_consumption}')
print(f'The total cost of transporting goods is: {total_cost:.2f}')