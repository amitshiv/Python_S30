# ==========================================
# Python Sets - Removing Duplicate Data
# ==========================================

# Example 1: Numbers
numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60]

# Print original list
print("Original list:", numbers)

# Convert list into a set
unique_numbers = set(numbers)

# Print unique values
print("Unique values:", unique_numbers)

# Convert set back into a list
unique_list = list(unique_numbers)

# Print unique list
print("Unique list:", unique_list)

# Count original elements
original_count = len(numbers)

# Count unique elements
unique_count = len(unique_numbers)

print("Original element count:", original_count)
print("Unique element count:", unique_count)


# ==========================================
# Example 2: Duplicate Student Names
# ==========================================

students = [
    "Rahul",
    "Amit",
    "Priya",
    "Rahul",
    "Sneha",
    "Amit",
    "Priya",
    "Vikas"
]

# Print original student list
print("\nOriginal student list:", students)

# Convert list into a set
unique_students = set(students)

# Print unique students
print("Unique students:", unique_students)

# Convert set back into a list
unique_student_list = list(unique_students)

# Print unique student list
print("Unique student list:", unique_student_list)

# Count original student records
student_record_count = len(students)

# Count unique students
unique_student_count = len(unique_students)

print("Total student records:", student_record_count)
print("Unique student count:", unique_student_count)