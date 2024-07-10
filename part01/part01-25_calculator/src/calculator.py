# Write your solution here
number1 = int(input("Number 1:"))
number2 = int(input("Number 2:"))
op = input("Operation:")

if op == "add":
    print(f"{number1} + {number2} = {number1 + number2}")
if op == "subtract":
    print(f"{number1} - {number2} = {number1 - number2}")
if op == "multiply":
    print(f"{number1} * {number2} = {number1 * number2}")