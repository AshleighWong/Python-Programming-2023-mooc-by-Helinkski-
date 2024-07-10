# Write your solution here

hourly_w = float(input("Hourly wage:"))
hours = int(input("Hours worked:"))
day = input("Day of the week:")

daily_w = hourly_w * hours

if day == "Sunday":
    print("Daily wages:", daily_w *2, "euros")
else:
    print("Daily wages:", daily_w, "euros")
