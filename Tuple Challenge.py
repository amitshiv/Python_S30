# ==========================================
# Python Tuples - Immutable Collection
# ==========================================

# Create a tuple of technologies.
# A tuple can contain duplicate values.
technologies = ("Python", "Java", "Python", "C++", "JavaScript", "Python")


# ==========================================
# 1. Print the Tuple
# ==========================================

print("Tuple:", technologies)


# ==========================================
# 2. Print the Type
# ==========================================

print("Type:", type(technologies))


# ==========================================
# 3. Print the First Item
# ==========================================

print("First item:", technologies[0])


# ==========================================
# 4. Print the Last Item
# ==========================================

print("Last item:", technologies[-1])


# ==========================================
# 5. Slice the Tuple
# ==========================================

# Get items from index 1 up to, but not including, index 4.
sliced_tuple = technologies[1:4]

print("Sliced tuple:", sliced_tuple)


# ==========================================
# 6. Count "Python"
# ==========================================

# count() tells us how many times a value appears.
python_count = technologies.count("Python")

print("Python count:", python_count)


# ==========================================
# 7. Find the Index of "C++"
# ==========================================

# index() returns the position of the first occurrence.
cpp_index = technologies.index("C++")

print("Index of C++:", cpp_index)


# ==========================================
# 8. Find Tuple Length
# ==========================================

# len() tells us the total number of items.
tuple_length = len(technologies)

print("Tuple length:", tuple_length)


# ==========================================
# 9. Convert Tuple into a List
# ==========================================

# Tuples cannot be directly modified.
# Convert it into a List when we need to add or change data.
technology_list = list(technologies)

print("Converted to list:", technology_list)


# ==========================================
# 10. Add "Go" to the List
# ==========================================

technology_list.append("Go")

print("List after adding Go:", technology_list)


# ==========================================
# 11. Convert List Back into a Tuple
# ==========================================

# Convert the modified List back into a Tuple.
technologies = tuple(technology_list)

print("Final tuple:", technologies)


# ==========================================
# 12. Immutability Demonstration
# ==========================================

# Tuples are immutable, which means their existing
# items cannot be changed, added, or removed directly.
#
# The following line would cause an error:
#
# technologies[0] = "C"
#
# TypeError: 'tuple' object does not support item assignment
#
# If we need to modify a tuple:
# Tuple -> List -> Modify -> Tuple