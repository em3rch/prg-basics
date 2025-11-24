###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if 18 <= points <= 20:
        grade = 'Excellent'
    elif 14 <= points < 18:
        grade = 'Good'
    elif 10 <= points < 14:
        grade = 'Satisfactory'
    elif 0 <= points < 10:
        grade = 'Fail'
    else:
        print("Error")
        exit(1)

    return grade


test_result = int(input("Enter scored points: "))
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')
