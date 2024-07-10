#Write your solution here
def squared(text, size):
    # i = 1
    # length = len(text)
    # word1 = text[0:size]
    # print(word1)
    # while i < size:
    #     displacement = length - size
    #     word2 = text[size:] + text[0:size-displacement]
    #     print(word2)
    #     i+=1

    i=0
    index = 0
    j=0
    while i < size:
        index = 0
        while index < size:
            if j > len(text)-1:
                j = 0
            print(text[j], end = "")
            index+=1
            j+=1
        print()
        i+=1


if __name__ == "__main__":
    squared("aybabtu", 5)
