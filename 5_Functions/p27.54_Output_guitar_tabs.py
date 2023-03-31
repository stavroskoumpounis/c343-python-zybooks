def generate_tablature(chords):
    chord_dict = {"G": [3, 0, 0, 0, 2, 3], "C": [0, 1, 0, 2, 3, -1], "D": [2, 3, 2, 0, -1, -1]}

    e_str = "e|-"
    B_str = "B|-"
    G_str = "G|-"
    D_str = "D|-"
    A_str = "A|-"
    E_str = "E|-"

    for chord in chords:
        fingering = chord_dict.get(chord)

        e_str += f"{fingering[0]}-"
        B_str += f"{fingering[1]}-"
        G_str += f"{fingering[2]}-"
        D_str += f"{fingering[3]}-"
        A_str += f"{fingering[4]}-" if fingering[4] != -1 else "--"
        E_str += f"{fingering[5]}-" if fingering[5] != -1 else "--"

    print(e_str)
    print(B_str)
    print(G_str)
    print(D_str)
    print(A_str)
    print(E_str)


num_chords = int(input("Enter number of chords: "))
chords = input(f"Enter {num_chords} chords separated by spaces: ").split()

generate_tablature(chords)
