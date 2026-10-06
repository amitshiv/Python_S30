# ==========================================
# Python Nested Lists
# Student Database Example
# ==========================================

# Create a nested list
students = [
    ["Rahul", 21, "Python"],
    ["Priya", 22, "Data Science"],
    ["Aman", 20, "Machine Learning"]
]


# 1. Print the complete list
print("Complete Student List:")
print(students)


# 2. Print Rahul's name
print("\nRahul's Name:")
print(students[0][0])


# 3. Print Priya's age
print("\nPriya's Age:")
print(students[1][1])


# 4. Print Aman's course
print("\nAman's Course:")
print(students[2][2])


# 5. Print Priya's complete record
print("\nPriya's Complete Record:")
print(students[1])


# 6. Change Rahul's course to AI
students[0][2] = "AI"

print("\nAfter Changing Rahul's Course:")
print(students)


# 7. Add another student manually
students.append(["Neha", 23, "Generative AI"])


# 8. Print the updated nested list
print("\nUpdated Student List:")
print(students)