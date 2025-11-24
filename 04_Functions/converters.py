def m_to_cm(n) -> int:
    return n*100

def cm_to_m(n) -> float | int:
    return n/100

def cm_to_inch(n) -> float | int:
    return n / 2.54

def foot_and_inch_to_cm(feet: int, inches: int) -> float:
    return (12 * feet) * 2.54 + (inches * 2.54)



if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'5\'11 = {foot_and_inch_to_cm(5, 11)}cm')
    print(f'532cm = {cm_to_inch(532)}inches')



