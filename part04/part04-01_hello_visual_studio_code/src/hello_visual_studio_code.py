# Write your solution here

def editor_use():
    while True:
        editor = input("Editor:")
        if editor.lower() == "visual studio code":
            break
        elif editor.lower() == "word" or editor.lower() == "notepad":
            message = "awful"
        else:
            message = "not good"
        print(message)
    print("an excellent choice!")

editor_use()