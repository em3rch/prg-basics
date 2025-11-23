print("SURVEY")
question1: str = input("Are you interested in computer science? (y/n): ")
question2: str = input("Do you like playing computer games? (y/n): ")
question3: str = input("Do you have an Instagram account? (y/n): ")

ans_lst: list = []
ans_lst += question1, question2, question3

res_lst: list = []


for i in ans_lst:
    if len(i) == 1:
        if i == 'y':
            res_lst.append("Yes")
        elif i == 'n':
            res_lst.append("No")
        else:
            print("Incorrect symbol.")
            exit(1)
    else:
        print("Answer is more than 1 character long.")
        exit(1)

print()
print(f"SURVEY RESULTS\n"
      f"Interested in computer science: {res_lst[0]}\n"
      f"Playing computer games: {res_lst[1]}\n"
      f"Has an Instagram account: {res_lst[2]}")


            
