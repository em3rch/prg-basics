def input_string(text: str) -> str:
    return input(text)

def input_integer(text: str) -> int:
    return int(input(text))

def input_real(text: str) -> float:
    return float(input(text))

def input_boolean(text: str) -> bool:
    inp = input(text)

    if len(inp) == 1:
        if inp == 'y':
            return True
        elif inp == 'n':
            return False
        else:
            print("Incorrect symbol entered.")
            exit(1)
    else:
        print("Entered symbol is more than 1 character long.")
        exit(1)

