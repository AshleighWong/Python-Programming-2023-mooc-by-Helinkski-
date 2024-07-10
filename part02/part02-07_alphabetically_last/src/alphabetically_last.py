# Write your solution here

word1 = input("Please type in the 1st word:")
word2 = input("Please type in the 2nd word:")

if word1 < word2:
    print(word2, "comes alphabetically last.")
elif word2 < word1:
    print(word1, "comes alphabetically last.")
else:
    print("You have the same word twice.")