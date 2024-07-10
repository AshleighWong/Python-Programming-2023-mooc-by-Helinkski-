# Write your solution here
string = input("Please type in a string:")
substring = input("Please type in a substring:")

index = string.find(substring)
new_string = string[index+len(substring):]
if substring in new_string:
    new_index = new_string.find(substring)
    print(f"The second occurrence of the substring is at index {new_index + index + len(substring)}.")
else:
    print("The substring does not occur twice in the string.")
