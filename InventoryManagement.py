# Inventory and Supply Chain Management

warehouses = {
    "Warehouse A": {"Laptop": 20, "Phone": 15, "Mouse": 5},
    "Warehouse B": {"Laptop": 10, "Phone": 25, "Mouse": 12},
    "Warehouse C": {"Laptop": 5, "Phone": 10, "Mouse": 20}
}

suppliers = {
    "Laptop": "Dell Supplier",
    "Phone": "Samsung Supplier",
    "Mouse": "Logitech Supplier"
}

# Inputs given directly in the code
product = "Laptop"
quantity = 8
source = "Warehouse A"
destination = "Warehouse B"
reorder_level = 5


# Add product
warehouses[source][product] = warehouses[source].get(product, 0) + quantity
print("Added:", quantity, product, "to", source)

# Remove product
remove_quantity = 3
if warehouses[source].get(product, 0) >= remove_quantity:
    warehouses[source][product] -= remove_quantity
    print("Removed:", remove_quantity, product, "from", source)

# Transfer stock
transfer_quantity = 5
if warehouses[source].get(product, 0) >= transfer_quantity:
    warehouses[source][product] -= transfer_quantity
    warehouses[destination][product] = \
        warehouses[destination].get(product, 0) + transfer_quantity
    print("Transferred:", transfer_quantity, product,
          "from", source, "to", destination)

# Reorder / low-stock detection
print("\nLow Stock Products:")
for warehouse, products in warehouses.items():
    for item, stock in products.items():
        if stock <= reorder_level:
            print(warehouse, "-", item, "Stock:", stock,
                  "-> Reorder required")

# Supplier management
print("\nSupplier:")
print(product, "->", suppliers[product])

# Automatic warehouse selection
order_quantity = 7
selected_warehouse = None

for warehouse, products in warehouses.items():
    if products.get(product, 0) >= order_quantity:
        selected_warehouse = warehouse
        break

print("\nWarehouse selected for order:")
if selected_warehouse:
    print(selected_warehouse)
else:
    print("No warehouse has sufficient stock")

# Display final inventory
print("\nFinal Inventory:")
for warehouse, products in warehouses.items():
    print(warehouse, ":", products)
