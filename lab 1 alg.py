# Option 9.
# Write a program that reads a sequence of numbers from a file, displays it on the screen,
# adding a dash after each number, how many times the digit entered from the keyboard was found in it
import time
flag = False
characters_limit = 1000000         #limit of characters in a file to read
digit = input("enter digit: ")
while not len(digit) == 1 or not digit.isdigit():       # checkin6g the condition "digit entered?"
    digit = input("enter digit: ")
start = time.time()
with open("file.txt", "r", encoding="utf-8") as file:       # workimg with file
    content = file.read()
    file_eof = file.read()
    i = 0
    if not content:                           # if file is empty
        print("\nFile text.txt in the project directory is empty.\nAdd a non-empty file to the directory or rename an existing one *.txt файл.")

    while len(content) > i:

        if i > characters_limit:                         #conditional limit on the number of characters in a file to read
            print("\nThe maximum number of characters read from the file. The program has finished working")
            break
        while len(content) > i and not content[i].isdigit():    #if symbol is not digit, skip it
            i += 1
        count = 0
        while len(content) > i and content[i].isdigit():
            print(content[i], end="")
            flag = True
            if content[i] == digit:             # if symbol is digit, count+1
                count += 1
            i += 1
        if flag == True:
            print(f"-{count}", end=" ")             # print count
if flag == False:
    print("\nFile text.txt in the project directory does not have numbers.")
if file_eof == '':                          # end of file
    print('\nEnd of file')
finish = time.time()
result = finish - start
print("Program time: " + str(result) + " seconds.")

