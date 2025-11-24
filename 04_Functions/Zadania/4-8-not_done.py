def time_string(hours: str, minutes: str, time_format: str):
    if (hours.isdigit() and len(str(hours)) == 2) and (minutes.isdigit() and len(str(minutes)) == 2):
        if time_format == "12":
            pm_am = ""

            if 


        
    else:
        print("Incorrect input values")
        exit(1)






hours = input("Enter hours (0..23): ")
minutes = input("Enter minutes (0..59): ")
time_format = input("Enter hours ('12' for 12-hour format or '24'): ")

result = time_string(hours=hours, minutes=minutes, time_format=time_format)

print(f"Time converted to {format}-hour format: {result}")

