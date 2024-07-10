# Write your solution here
def everything_reversed(my_list:list):
    new = []
    for item in my_list[::-1]:
        new.append(item[::-1])
    return new

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)