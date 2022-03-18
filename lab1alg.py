# Option 9.
# Write a program that reads a sequence of numbers from a file, displays it on the screen,
# adding a dash after each number, how many times the digit entered from the keyboard was found in it
digit = input("enter digit: ")
# checking the condition "digit entered?"
while not len(digit) == 1 or not digit.isdigit():
    digit = input("enter digit: ")
# workimg with file
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    i = 0
    if not content:  # if file is empty
        print("\nFile text.txt in the project directory is empty.\nAdd a non-empty file to the directory or rename an existing one *.txt файл.")
    while len(content) > i:
        while len(content) > i and not content[i].isdigit():    #if symbol is not digit, skip
            i += 1
        count = 0

        while len(content) > i and content[i].isdigit():
            print(content[i], end="")
            if content[i] == digit:             # if symbol is digit, count+1
                count += 1
            i += 1

        print(f"-{count}", end=" ")             # print count

