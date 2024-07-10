# Write your solution here

value = int(input("Value of gift:"))
lower_limit = 0
lower_tax_limit = 0
percent = 0

taxed = True

if value < 5000:
    print("no tax!")
    taxed = False
elif value < 25000:
    lower_tax_limit = 100
    lower_limit = 5000
    percent = .08
elif value < 55000:
    lower_tax_limit = 1700
    lower_limit = 25000
    percent = .10
elif value < 200000:
    lower_tax_limit = 4700
    lower_limit = 55000
    percent = .12
elif value < 1000000:
    lower_tax_limit = 22100
    lower_limit = 200000
    percent = .15
else:
    lower_tax_limit = 142100
    lower_limit = 1000000
    percent = .17

tax = (lower_tax_limit + (value - lower_limit) * percent)

if taxed:
    print("Amount of tax:", tax, "euros")



