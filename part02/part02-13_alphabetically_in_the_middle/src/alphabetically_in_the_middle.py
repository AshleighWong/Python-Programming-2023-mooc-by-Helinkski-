# Write your solution here

letter1 = input("1st letter:")
letter2 = input("2nd letter:")
letter3 = input("3rd letter:")

middle = ""
if letter1 > letter2 and letter1 > letter3:
    if letter2 > letter3:
        middle = letter2
    else:
        middle = letter3
elif letter1 < letter2 and letter1 < letter3:
    if letter2 < letter3:
        middle = letter2
    else:
        middle = letter3
else:
    middle = letter1

print("The letter in the middle is", middle)
