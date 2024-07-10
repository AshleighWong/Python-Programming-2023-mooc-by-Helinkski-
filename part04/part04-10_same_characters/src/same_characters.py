# Write your solution here
def same_chars(string, i, j):
    if i >= len(string) or j >= len(string):
        return False
    elif string[i] == string[j]:
        return True
    return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("coder", 1, 10))