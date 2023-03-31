clients_per_minute = list(map(int, input("Enter list of customers for 10 min :").split()))

current_minute = 0
clients = 0

for minute in range(10):
    clients += clients_per_minute[minute]
    print(f" Minute {minute} : clients to be served: {clients}")
    if clients != 0:
        clients -= 1
        print(" 1 client was served", end=",")
    print(f" {clients} remaining")

