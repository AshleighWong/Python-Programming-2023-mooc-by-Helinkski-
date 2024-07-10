# Write your solution here

number = int(input("Number:"))
word = ""

if number%3 == 0  and number%5 == 0:
    word = "Fizzbuzz"
elif number%3 == 0:
    word = "Fizz"
elif number%5 == 0:
    word = "Buzz"

print(word)


