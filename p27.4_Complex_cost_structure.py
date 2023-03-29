"""
An airline describes airfare as follows. A normal ticket's base cost is $300. Persons aged 60 or over have a base
cost of $290. Children 2 or under have $0 base cost. A carry-on bag costs $10. A first checked bag is free,
second is $25, and each additional is $50. Given inputs of age, carry-on (0 or 1), and checked bags (0 or greater),
compute the total airfare.
"""

passengerAge = int(input("Input the passenger's age ="))
carryOns = int(input("Input the num for carry ons(0 or 1) ="))
checkedBags = int(input("Input the num of checked bags(0 or greater) ="))

baseTicketCost = 290 if passengerAge >= 60 else 0 if passengerAge <= 2 else 300
carryOnCost = 10 if carryOns == 1 else 0

checkedBagsCost = 0
if checkedBags > 0:
    checkedBagsCost = 25
if checkedBags > 1:
    checkedBagsCost += 50 * (checkedBags-1)

totalFare = baseTicketCost + carryOnCost + checkedBagsCost

print(totalFare)
