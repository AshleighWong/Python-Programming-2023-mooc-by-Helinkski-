# Write your solution here
word = input("Please type in a word:")
character = input("Please type in a character:")
index = word.find(character)
if index >=0 and (len(word) - 1 - index) > 2:
    print(word[index:index+3])#print from the first index of substring to end
