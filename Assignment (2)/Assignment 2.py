# Creating variables and dictionaries
total = 0
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# Stock information was not given in question 2 so information taken from question 3
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

# Calculates and prints total and individual information
for a,b in prices.items():
    print(a,"\nprice:",b,"\nstock:",stock[a],"\n")
    total += b*stock[a]
print("Total=",total)