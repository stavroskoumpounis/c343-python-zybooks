def max_five(a, b, c, d, e):
    five_list = [a, b, c, d, e]
    maxi = a
    for i in range(1, 5):
        if five_list[i] > maxi:
            maxi = five_list[i]
    return maxi


list_f = [int(x) for x in input("Enter a list : ").split()]

print("Max is ", max_five(* list_f))
