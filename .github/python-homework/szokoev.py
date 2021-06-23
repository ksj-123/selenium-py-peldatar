x = int(input())

if x % 4 != 0:
    print("Nem szökőév")
elif x % 4 == 0:
    print("Szökőév")
    if x % 400 == 0:
        print("Szökőév")
    elif x % 100 == 0:
        print("Nem szökőév")

