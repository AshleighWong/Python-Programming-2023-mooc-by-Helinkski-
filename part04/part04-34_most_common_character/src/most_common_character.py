# Write your solution here
def most_common_character(string: str):
    char = " "
    count = 0
    for x in string:
        if string.count(x) > count:
            count = string.count(x)
            char = x
    return char

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))