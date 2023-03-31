my_list = [int(x) for x in input("Enter a list of vals: ").split()]
print("List before : ", my_list)

start = 0
end = len(my_list) - 1

while start <= end:
    temp = my_list[start]
    my_list[start] = my_list[end]
    my_list[end] = temp
    start += 1
    end -= 1

print("List after : ", my_list)
