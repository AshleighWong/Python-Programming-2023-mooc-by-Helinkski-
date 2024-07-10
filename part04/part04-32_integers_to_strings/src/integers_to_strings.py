# Write your solution here
def formatted(my_list:list):
    new = []
    for x in my_list:
        x = f"{x:.2f}"
        new.append(x)
    return new

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)