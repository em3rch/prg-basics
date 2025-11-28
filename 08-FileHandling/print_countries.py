###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    line_counter = 1 
    for line in file:
        print(f"{line_counter}. {line}", end='')
        line_counter += 1