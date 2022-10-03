def append(text):
    file = open("data.txt", "a")
    file.write(text + "\n")
    file.close()

def prepend(text):
    read_files = open("data.txt")
    lines = read_files.readlines()
    lines.insert(0, text + "\n")
    file = open("data.txt", "w")
    file.write("".join(lines))
    file.close()

prepend(input(""))
