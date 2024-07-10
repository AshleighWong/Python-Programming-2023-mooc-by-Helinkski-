# Write your solution here
def no_vowels(string:str):
    new = string.replace("a", "")
    new = new.replace("e", "")
    new = new.replace("i", "")
    new = new.replace("o", "")
    new = new.replace("u", "")
    return new

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))