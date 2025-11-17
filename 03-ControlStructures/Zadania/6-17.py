time_24_hour_format = input("Enter time (24-hour format '00:00'): ")
pm_am = ''


hours = time_24_hour_format[0:2]
minutes = time_24_hour_format[3:]

if hours.isdigit() and len(hours) == 2 and minutes.isdigit() and len(minutes) == 2:
    if 0 < int(hours) < 12:
        pm_am = "a.m."
    elif 12 < int(hours) < 24:
        pm_am = "p.m."
        hours = str(int(hours) - 12)
        if hours[0] != '0':
            hours = '0' + hours
    elif int(hours) == 12 and int(minutes) == 0:
        pm_am = "noon"
    elif int(hours) == 12:
        pm_am = "p.m."
else:
    print("Incorrect time format.")
    exit(1)

print(f"Time in 12-hour format: {hours}:{minutes} {pm_am}")





