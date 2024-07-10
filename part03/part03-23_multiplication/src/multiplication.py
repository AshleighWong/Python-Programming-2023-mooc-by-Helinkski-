# Write your solution here

number = int(input("Please type in a number:"))
i= 0
while i < number:
    i +=1
    j = 1
    while j <= number:
        print(f"{i} x {j} = {i*j}")
        j+=1
