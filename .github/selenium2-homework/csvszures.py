with open("table_in.csv", 'r', encoding="utf-8") as infile:
    with open("table_out.csv", 'w', encoding="utf-8") as outfile:
        sor = infile.readline()
        # lista = infile.read().replace("\n", " ").replace(" ", "").split(",")
        while sor:
            outfile.write(sor)
            sor = infile.readline()
            # for i, word in list(enumerate(sor))[1:]:
            #     sor.write(f"{i + 1}, {word}\n")


