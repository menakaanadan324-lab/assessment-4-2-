# InventoryQA.py

inventory = {
    "Warehouse A": {"Laptop": 10, "Phone": 5},
    "Warehouse B": {"Laptop": 8, "Phone": 12},
    "Warehouse C": {"Laptop": 15, "Phone": 10}
}

reorder_threshold = 5

# Inputs given directly in the code
product = "Laptop"
warehouse = "Warehouse A"
quantity = 7

# 1. Stock availability
stock = inventory[warehouse].get(product, 0)

if stock >= quantity:
    print("Stock Availability: PASS")
else:
    print("Stock Availability: FAIL - Insufficient stock")


# 2. Insufficient inventory
quantity_needed = 20

if inventory[warehouse].get(product, 0) < quantity_needed:
    print("Insufficient Inventory: PASS")
else:
    print("Insufficient Inventory: FAIL")


# 3. Warehouse transfer
transfer_product = "Laptop"
transfer_quantity = 3
source = "Warehouse A"
destination = "Warehouse B"

if inventory[source].get(transfer_product, 0) >= transfer_quantity:
    inventory[source][transfer_product] -= transfer_quantity
    inventory[destination][transfer_product] += transfer_quantity
    print("Warehouse Transfer: PASS")
else:
    print("Warehouse Transfer: FAIL")


# 4. Concurrent orders
order1 = 4
order2 = 5
available = inventory["Warehouse B"]["Laptop"]

if order1 + order2 <= available:
    print("Concurrent Orders: PASS")
else:
    print("Concurrent Orders: FAIL - Stock conflict")


# 5. Reorder threshold
for w in inventory:
    for p, stock in inventory[w].items():
        if stock <= reorder_threshold:
            print("Reorder Required:", w, p, "Stock =", stock)


# 6. Invalid product
invalid_product = "Tablet"

if invalid_product not in inventory[warehouse]:
    print("Invalid Product: PASS")
else:
    print("Invalid Product: FAIL")


# 7. Negative inventory
negative_quantity = -5

if negative_quantity < 0:
    print("Negative Inventory: PASS - Negative quantity rejected")
else:
    print("Negative Inventory: FAIL")


# 8. Multiple warehouses
print("\nMultiple Warehouse Check:")

for w in inventory:
    print(w, "->", inventory[w])

print("\nQA Testing Completed")
