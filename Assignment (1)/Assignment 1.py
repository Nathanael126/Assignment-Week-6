# Creating Inventory Dictionary with Pocket and items
inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone','dagger', 'bedroll','bread loaf'],
    'pocket': ['seashell','strange berry','lint']
}

# Sort and remove elements from backpack, and adds gold
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

# Prints results
for a,b in inventory.items():
    print(a,": ",b)