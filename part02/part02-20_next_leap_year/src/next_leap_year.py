# Write your solution here

year = int(input("Year:"))
old_year = year
while True:
    year +=1
    if year%100 == 0:
        if year%400 == 0:
            break
    elif year%4 == 0:
        break

print(f"The next leap year after {old_year} is {year}")