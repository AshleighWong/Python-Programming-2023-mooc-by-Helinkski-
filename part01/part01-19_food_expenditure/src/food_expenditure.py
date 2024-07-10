# Write your solution here
num_times = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))

weekly_cost = (price*num_times) + groceries
print("Average food expenditure:")
print(f"Daily: {weekly_cost/7} euros")
print(f"Weekly: {weekly_cost} euros")
