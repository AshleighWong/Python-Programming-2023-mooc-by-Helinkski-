# Write your solution here

def sum_of_positives(my_list: list):
    sums = 0
    for x in my_list:
        if x > 0:
            sums += x
    return sums


if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)