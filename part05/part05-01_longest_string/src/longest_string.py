# Write your solution here
def longest(strings:list):
    longest = strings[0]
    for x in strings:
        if len(x) > len(longest):
            longest = x
    return longest

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))