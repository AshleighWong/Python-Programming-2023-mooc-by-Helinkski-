# Write your solution here
sentence = input("Please type in a sentence")
sentence = " " + sentence
index = 0
while index!=-1:
    index = sentence.find(" ")
    if index != -1:
        print(sentence[index+1])
        sentence = sentence[index+1:]
