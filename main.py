#Option 9.
#Write a program that reads a sequence of numbers from a file, displays it on the screen,
# adding a dash after each number, how many times the digit entered from the keyboard was found in it
print("enter digit: ")
digit = input()
#checking the condition "digit entered?"
while not len(digit) == 1 or not digit.isdigit():
    digit = input("enter digit: ")
#workimg with file
with open("C:Users\\USER\\Desktop\\123.txt", "r") as file:
    content = file.read()
    i = 0
    while len(content) > i:
        while len(content) > i and not content[i].isdigit():
            print(content[i], end="")
            i += 1

        count = 0
        while len(content) > i and content[i].isdigit():
            print(content[i], end="")
#if symbol is digit, count+1
            if content[i] == digit:
                count += 1
            i += 1
        print(f"-{count}", end="")