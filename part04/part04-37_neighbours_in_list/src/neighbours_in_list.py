# Write your solution here

def longest_series_of_neighbours(my_list: list):
    new = []
    old = my_list[0]
    longest = 0
    for x in my_list:
        if old-x == -1 or old-x == 1:
            new.append(x)
        else:
            new.clear()
        if longest < len(new):
            longest = len(new)
        old = x
    #longest = len(new)
    return longest + 1
    
if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))