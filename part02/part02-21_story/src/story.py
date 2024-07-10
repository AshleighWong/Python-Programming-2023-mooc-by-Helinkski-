# Write your solution here

story = ""
old_word = ""
while True:
    word = input("Please type in a word:")
    if word == "end":
        break
    elif word == old_word:
        break
    old_word = word
    story += word + " "

print(story)