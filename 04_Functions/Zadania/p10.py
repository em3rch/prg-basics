def f(time1, time2):
    hours1, hours2 = time1[0:2], time2[0:2]
    minutes1, minutes2 = time1[3:], time2[3:]

    end_hours_minutes = ""

    if hours1 < hours2:
        end_hours_minutes = hours1 + ":" + minutes1
    elif hours1 == hours2:
        if minutes1 < minutes2:
            end_hours_minutes = hours1 + ":" + minutes1
        else:
            end_hours_minutes = hours2 + ":" + minutes2
    else:
        end_hours_minutes = hours2 + ":" + minutes2

    return end_hours_minutes


if __name__ == "__main__":
    print(f("21:42", "21:41"))