# ==========================================
# Python List Methods
# Shopping Cart Example
# ==========================================

# Create the shopping cart
cart = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]


# 1. Display all products
print("All Products:")
print(cart)


# 2. Access first product
print("\nFirst Product:")
print(cart[0])


# 3. Access last product
print("\nLast Product:")
print(cart[-1])


# 4. Add Webcam at the end
cart.append("Webcam")
print("\nAfter append():")
print(cart)


# 5. Insert USB Hub at index 2
cart.insert(2, "USB Hub")
print("\nAfter insert():")
print(cart)


# 6. Remove Mouse
cart.remove("Mouse")
print("\nAfter remove():")
print(cart)


# 7. Remove the last item using pop()
removed_product = cart.pop()

print("\nRemoved using pop():")
print(removed_product)

print("\nCart after pop():")
print(cart)


# 8. Find the index of Monitor
monitor_index = cart.index("Monitor")

print("\nIndex of Monitor:")
print(monitor_index)


# 9. Count occurrences of Laptop
laptop_count = cart.count("Laptop")

print("\nNumber of Laptops:")
print(laptop_count)


# 10. Create a copy of the cart
backup_cart = cart.copy()

print("\nCopied Cart:")
print(backup_cart)


# 11. Reverse the cart
cart.reverse()

print("\nAfter reverse():")
print(cart)


# 12. Sort products alphabetically
cart.sort()

print("\nAfter sort():")
print(cart)


# ==========================================
# Additional Method Examples
# ==========================================

# append() - add one item
cart.append("Charger")


# extend() - add multiple items
cart.extend(["Cable", "Power Bank"])

print("\nAfter extend():")
print(cart)


# insert() - add at a specific position
cart.insert(1, "USB Cable")

print("\nAfter insert():")
print(cart)


# remove() - remove by value
cart.remove("Power Bank")

print("\nAfter remove():")
print(cart)


# pop() - remove last item
cart.pop()

print("\nAfter pop():")
print(cart)


# copy() - create another list
new_cart = cart.copy()

print("\nCopied Cart:")
print(new_cart)


# clear() - remove everything
cart.clear()

print("\nAfter clear():")
print(cart)