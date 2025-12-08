###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers
# calculates the number of incorrect answers

correct_answers = 0
incorrect_answers = 0

for answer in test_results:
    if answer == True:
        correct_answers += 1
    else:
        incorrect_answers += 1

# calculates the percentage of correct answers
...

print('TEST STATISTICS')
print('===============')
print('Number of questions: ', len(test_results)) 
print('Number of correct answers: ', correct_answers)
print('Number of incorrect answers: ', incorrect_answers)
print('Percentage of correct answers: ', correct_answers * 100 / question_number)