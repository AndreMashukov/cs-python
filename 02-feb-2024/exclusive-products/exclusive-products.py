# You have two lists named inventory1 and inventory2 representing the clothing items from these stores. 
# Now, your prime mission is to figure out the clothes that are exclusive to each store.

def exclusive_products(inventory1, inventory2):
    # implement this
    inventory1 = [x.upper() for x in inventory1]
    inventory2 = [x.upper() for x in inventory2]
    exclusive_inventory1 = []
    exclusive_inventory2 = []
    for item in inventory1:
        if item not in inventory2:
            exclusive_inventory1.append(item)
        else:
            inventory2.remove(item)
    exclusive_inventory2 = inventory2
    return exclusive_inventory1, exclusive_inventory2

inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])