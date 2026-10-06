# ==========================================
# List of Dictionaries - Product Dataset
# ==========================================

# Create a List containing three Dictionaries.
# Each Dictionary represents one product.
products = [
    {
        "name": "Laptop",
        "price": 70000,
        "brand": "Dell"
    },
    {
        "name": "Phone",
        "price": 40000,
        "brand": "Samsung"
    },
    {
        "name": "Tablet",
        "price": 30000,
        "brand": "Apple"
    }
]


# ==========================================
# 1. Print All Products
# ==========================================

print("All Products:")
print(products)


# ==========================================
# 2. Print First Product
# ==========================================

# List indexing starts from 0.
# Index 0 represents the first product.
print("\nFirst Product:")
print(products[0])


# ==========================================
# 3. Print Second Product's Price
# ==========================================

# First access the second Dictionary using index 1.
# Then use the "price" key to access its value.
print("\nSecond Product Price:")
print(products[1]["price"])


# ==========================================
# 4. Print Third Product's Brand
# ==========================================

# Index 2 represents the third product.
# "brand" is the key used to access the brand value.
print("\nThird Product Brand:")
print(products[2]["brand"])


# ==========================================
# 5. Change First Product's Price
# ==========================================

# Access the first product using index 0,
# then access the "price" key and update its value.
products[0]["price"] = 75000

print("\nUpdated First Product:")
print(products[0])


# ==========================================
# 6. Add Rating to the Second Product
# ==========================================

# Add a new key-value pair to the second product.
products[1]["rating"] = 4.5

print("\nUpdated Second Product:")
print(products[1])


# ==========================================
# 7. Add Another Product Manually
# ==========================================

# append() adds a new Dictionary to the List.
products.append({
    "name": "Monitor",
    "price": 25000,
    "brand": "LG"
})

print("\nAfter Adding Another Product:")
print(products)


# ==========================================
# 8. Print Final Dataset
# ==========================================

print("\nFinal Product Dataset:")
print(products)


# ==========================================
# Understanding the Structure
# ==========================================

# The outer structure is a LIST.
#
# products
#    ↓
# [
#     Dictionary 1,
#     Dictionary 2,
#     Dictionary 3,
#     Dictionary 4
# ]
#
# Each product is a DICTIONARY.
#
# Example:
#
# {
#     "name": "Laptop",
#     "price": 75000,
#     "brand": "Dell"
# }
#
# LIST → Used to store multiple products.
#
# INDEX → Used to identify a product.
# Example:
# products[0] → First product
# products[1] → Second product
# products[2] → Third product
#
# DICTIONARY → Used to store information about one product.
#
# KEY → Identifies the information.
# Example:
# "name"
# "price"
# "brand"
#
# VALUE → The actual information stored against a key.
# Example:
# "Laptop"
# 75000
# "Dell"
#
# To access a value:
#
# products[0]["name"]
#
# Step 1 → products[0]
#          Find the first product.
#
# Step 2 → ["name"]
#          Find the name inside that product.
#
# Result:
# Laptop
#
# Easy way to remember:
#
# LIST = Collection of products
# DICTIONARY = Details of one product
# INDEX = Finds the product
# KEY = Finds the detail
# VALUE = Actual data