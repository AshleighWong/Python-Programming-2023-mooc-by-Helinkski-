# Write your solution here

#using while loop
# def palindromes(string: str):
#     i=1
#     x=0
#     palindrome = True
#     while x < len(string)//2:
#         if string[x] != string[len(string) -i]:
#             palindrome = False
#             break
#         x+=1
#         i+=1
#     return palindrome

#using for loop
def palindromes(string: str):
    for x in range(len(string)//2):
        if string[x] != string[len(string)-x-1]:
            return False
    return True
        
def main():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word) == True:
            break
        print("that wasn't a palindrome")
    
    print(f"{word} is a palindrome!")
    
        
    
    
        
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

main()