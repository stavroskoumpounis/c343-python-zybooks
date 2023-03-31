"""Southern California's electric company uses a "three tier" cost structure for household electric bills. As of Jan
2017, for a given month, the first 232 kWh is $0.08291/kWh, the next 696 kWh is $0.16838/kWh, and any additional kWh
is $0.23336/kWh. Write a function that takes a household month's kWh, and the cutoffs and prices for the tiers,
and returns that month's electric cost."""

kwh, tier1_cutoff, tier1_rate, tier2_cutoff, tier2_rate, tier3_rate = [float(x) for x in input().split()]
tier2_cutoff += tier1_cutoff

if kwh <= tier1_cutoff:
    cost = kwh * tier1_rate
elif kwh <= tier2_cutoff:
    cost = tier1_cutoff * tier1_rate + (kwh - tier1_cutoff) * tier2_rate
else:
    cost = tier1_cutoff * tier1_rate + (tier2_cutoff - tier1_cutoff) * tier2_rate + (kwh -tier2_cutoff) * tier3_rate

print(f"${cost:.2f}")