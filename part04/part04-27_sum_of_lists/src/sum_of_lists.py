# Write your solution here
def list_sum (list1, list2: list):
    new = []
    sums = 0
    for x in range(len(list1)):
        sums = list1[x] + list2[x]
        new.append(sums)
    return new

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]