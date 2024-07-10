# Write your solution here

limit = int(input("Limit:"))
number = 1
sums = 0
while sums < limit:
    sums += number
    number += 1

print(sums)