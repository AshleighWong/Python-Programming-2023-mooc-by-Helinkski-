# Write your solution here

limit = int(input("Limit:"))
number = 1
sums = 1
string = "1"
while sums < limit:
    number +=1
    sums += number
    string += " + " + str(number) 

print(f"The consecutive sum: {string} = {sums}")