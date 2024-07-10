# Write your solution here

while True:
    string = input("Please type in a string:")
    length = len(string)
    if len(string) > 0:
        print(string)
        print("-"*length)
    else:
        break