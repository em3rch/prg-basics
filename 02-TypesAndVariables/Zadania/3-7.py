###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8_000_000_000
north = 7_200_000_000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", (north * 100) / total)
print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", (south * 100) / total)
