# Write your solution here
def all_the_longest(my_list:list):
    longest = my_list[0]
    new = []
    for x in my_list:
        if len(x) > len(longest):
            longest = x
            new.clear()
            new.append(x)
        elif len(x) == len(longest):
            if x not in new:
                new.append(x)
            if longest not in new:
                new.append(longest)
    return new

if __name__ == "__main__":
    print(all_the_longest(('Alan', 'Grace', 'Steve', 'Kim', 'Susan')))
