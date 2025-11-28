with open("../pets.txt", 'r') as file:
    content = file.read()

file_lines = content.splitlines()

word_counter = 0

for i in file_lines:
    word_counter += len(i.split())
    print(i)

print()
print(f"Number of words: {word_counter}")

