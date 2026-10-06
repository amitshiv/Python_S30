# ==========================================
# Remove Duplicate Data Using Sets
# ==========================================

# A List allows duplicate values, which is common when
# data comes from multiple sources or repeated records.
numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60]

# Display the original data so we can compare it
# with the data after duplicate removal.
print("Original list:", numbers)

# A Set stores only unique values.
# Converting the List to a Set automatically removes duplicates,
# making Sets useful when we need to identify unique data quickly.
unique_numbers = set(numbers)

# Display the Set to observe which duplicate values disappeared.
print("Unique values:", unique_numbers)

# Convert the Set back to a List when we need List functionality
# while keeping only the unique values.
unique_list = list(unique_numbers)

print("Unique list:", unique_list)

# Count all records in the original List.
# This tells us how many values were present before removing duplicates.
original_count = len(numbers)

# Count values in the Set.
# Because a Set contains only unique values, this gives us
# the number of unique records.
unique_count = len(unique_numbers)

print("Original element count:", original_count)
print("Unique element count:", unique_count)


# ==========================================
# Example 2: Duplicate Student Names
# ==========================================

# Duplicate student names may occur when data is collected
# from different classes, files, or registration records.
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

print("\nOriginal student list:", students)

# Convert the List to a Set to keep only one occurrence
# of each student name.
# This is useful when we want to know how many different
# students are present without manually checking duplicates.
unique_students = set(students)

print("Unique students:", unique_students)

# Convert the unique Set back to a List if the program
# needs the data in List format for further processing.
unique_student_list = list(unique_students)

print("Unique student list:", unique_student_list)

# Count the total number of student records before
# removing duplicate names.
student_record_count = len(students)

# Count the number of unique students.
# The Set automatically ignores repeated names.
unique_student_count = len(unique_students)

print("Total student records:", student_record_count)
print("Unique student count:", unique_student_count)


# ==========================================
# Key Idea:
# ==========================================

# List  -> Duplicates are allowed
# Set   -> Only unique values are stored
#
# Sets are useful when working with duplicate data because
# they provide a simple way to remove duplicates and find
# the number of unique values without writing a loop.
