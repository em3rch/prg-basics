categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]


print(f"The most expensive expense category "
      f"({max(expenses)}) is "
      f"{categories[expenses.index(max(expenses))]}")