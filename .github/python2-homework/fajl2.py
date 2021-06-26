with open("adat.txt", "r") as file:
    obs = int(file.readline())
    my_list = file.readline().split(" ")
    print(my_list)