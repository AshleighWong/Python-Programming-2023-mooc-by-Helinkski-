# Write your solution here
def shortest(my_list:list):
    new = []
    short = my_list[0]
    for x in my_list:
        if len(x) < len(short):
            short = x
    return short

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)