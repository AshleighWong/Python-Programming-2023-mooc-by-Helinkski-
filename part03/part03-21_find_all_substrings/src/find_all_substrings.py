# Write your solution here
word = input("Please type in a word:")
character = input("Please type in a character:")
# while True:
#     index = word.find(character)
#     if len(word) == 0 or index < 0: 
#         break
#     elif len(word) >= index+3:
#         print(word[index:index+3])
#     word = word[index+1:]

index = 0
while len(word) >= index+3:
    if word[index] == character:
        print(word[index:index+3])
    index +=1