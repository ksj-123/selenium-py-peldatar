with open("adat.txt", "r") as file:
    lines = file.readlines()
    for line in lines[:]:
        print(line.replace("\n", "").split(','))


