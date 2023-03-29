id_to_find = input()
found = False

with open('CustomerDb.txt', 'r') as customer_db:
    for line in customer_db:
        customer_info = line.split()
        if customer_info[0] == id_to_find:
            print(customer_info[1], customer_info[2])
            found = True
            break

if not found:
    print('Not found')
