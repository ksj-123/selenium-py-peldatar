nyit = open("adat.txt")

for sor in nyit:
    print(sor.strip() + " ", end="")

nyit.close()
print('')
