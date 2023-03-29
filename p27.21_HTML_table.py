input_rows = int(input())
input_cols = int(input())

print("<table>")

for row in range(input_rows):
    print("<tr>", end="")
    for col in range(input_cols):
        print(" <td> c </td>", end="")
    print(" </tr>")

print("</table>")