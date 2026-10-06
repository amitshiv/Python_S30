student = "python programming for data science"

# Print complete string
print("Complete string:", student)

# First character
print("First character:", student[0])

# Last character
print("Last character:", student[-1])

# First 6 characters
print("First 6 characters:", student[:6])

# Last 7 characters
print("Last 7 characters:", student[-7:])

# Reverse the string
print("Reversed string:", student[::-1])

# Uppercase
print("Uppercase:", student.upper())

# Lowercase
print("Lowercase:", student.lower())

# Title case
print("Title case:", student.title())

# Count "a"
print("Number of 'a':", student.count("a"))

# Find "programming"
print("Position of 'programming':", student.find("programming"))

# Replace data science
print(
    "After replacement:",
    student.replace(
        "data science",
        "artificial intelligence"
    )
)

# Split into words
print("Words:", student.split())