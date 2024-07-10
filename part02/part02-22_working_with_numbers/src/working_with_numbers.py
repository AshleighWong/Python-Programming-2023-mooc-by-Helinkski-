# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")
amount = 0
positive = 0
negative = 0
sums = 0
while True:
    number = int(input("Number:"))
    amount += 1
    sums += number
    if number > 0:
        positive +=1
    elif number < 0:
        negative +=1
    if number == 0:
        break

print(f"Numbers typed in {amount-1}")
print("The sum of the numbers is", sums)
print("The mean of the numbers is", sums/(amount-1))
print("Positive numbers", positive)
print("Negative numbers", negative)
