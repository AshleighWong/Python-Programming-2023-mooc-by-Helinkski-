# Write your solution here
def length_of_longest(my_list:list):
    longest = my_list[0]
    for x in my_list:
        if len(x) > len(longest):
            longest = x
    return len(longest)

if __name__ == "__main__":
    print(length_of_longest(('Alan', 'Grace', 'Frances', 'Kim', 'Susan')))
    
