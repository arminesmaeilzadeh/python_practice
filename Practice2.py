satr = int(input(" Satr: "))
soton = int(input("Soton: "))


# Initialize matrix
def mat(satr, soton):
    matrix = []
    print("Adad ha ra vared konid:")
    # Daryaft Vrodi

    for i in range(soton):
        a = []
        for j in range(satr):
            a.append(int(input()))
        matrix.append(a)

    # Print Eteleaat vared shode
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

    a = 0
    b = 0

    for i in matrix:
        if 0 in i:
            a = matrix.index(i) + 1

    for i in matrix[a - 1]:
        if i == 0:
            b = matrix[a - 1].index(i) + 1

    if a == 0 and b == 0:
        print(" 0 dar matrix vojud nadarad!")
    else:
        print(f" satr: {a} \n \bsoton: {b}")


mat(satr, soton)