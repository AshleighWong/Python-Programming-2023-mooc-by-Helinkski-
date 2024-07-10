# Write your solution here
number = int(input("Please type in a number:"))
i = 1
j = 0
if number == 1:
    print(1)
while i < number and i <= number - j:
    print(i)
    if i != number - j:
        print(number - j)
    j +=1
    i+=1