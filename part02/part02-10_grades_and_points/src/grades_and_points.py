# Write your solution here

points = int(input("How many points[0-100]:"))

if points < 0 or points > 100:
    print("impossible!")
elif points >= 0 and points <= 49:
    print("fail")
elif points < 60:
    print("Grade: 1")
elif points < 70:
    print("Grade: 2")
elif points < 80:
    print("Grade: 3")
elif points < 90:
    print("Grade: 4")
else:
    print("Grade: 5")