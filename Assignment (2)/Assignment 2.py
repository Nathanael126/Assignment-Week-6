total = 0
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for a,b in prices.items():
    print(a,"\nprice:",b,"\nstock:",stock[a],"\n")
    total += b*stock[a]
print("Total=",total)