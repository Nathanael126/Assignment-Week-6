# Defining compute_bill function
def compute_bill(a):
    total = 0
    for x in a:
        if x in stock:
            if stock[x] > 0:
                total += prices[x]
                stock[x] -= 1
    return total

# Create groceries list and create other dictionaries
groceries = ["banana","orange","apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Print the bill and individual information
print("Bill total: ", compute_bill(groceries),"\n")
for a,b in prices.items():
    print(a,"\nprice:",b,"\nstock:",stock[a],"\n")