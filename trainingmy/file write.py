p = 1
while (p != 0):
    text_file = open("file.txt", "a")
    first = input("First name:")
    second = input("Second name:")
    n = text_file.write(first + " " + second + "\n")
    p = int(input("Do you what to add more, press 1 or press 0 "))

text_file.close()
