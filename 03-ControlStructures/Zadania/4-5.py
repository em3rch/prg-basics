###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for i in plain_text:
    if i == ' ':
        encrypted_text += ' ' 
        continue
    # read the character's code (use ord())
    i_ascii_code = ord(i)
    # add one to the character's code
    i_ascii_code += 1
    # replace new character code with its
    # corresponding character (use chr())
    i_ascii_chr = chr(i_ascii_code)
    # add encrypted character to encrypted text
    encrypted_text += i_ascii_chr

print(f"plain_text: {plain_text}")
print(f"encrypted_text: {encrypted_text}")