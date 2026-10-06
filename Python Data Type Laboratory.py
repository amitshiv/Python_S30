# ============================================
# Python Data Types and Type Conversion
# ============================================

# -----------------------------
# 1. Creating Different Data Types
# -----------------------------

# Integer (int)
age = 29
students = 50
experience = 4

# Float (float)
height = 5.8
salary = 75000.50

# String (str)
name = "Amit"
city = "Bhopal"
course = "Python"

# Boolean (bool)
likes_python = True
is_student = False

# List
skills = ["Python", "SAP MM", "AI"]

# Tuple
coordinates = (23.25, 77.41)

# Set
unique_numbers = {1, 2, 2, 3, 4}

# Dictionary
student = {
    "name": "Amit",
    "age": 29,
    "city": "Bhopal"
}


# -----------------------------
# 2. Display Variables
# -----------------------------

print("----- VARIABLES -----")

print("Age:", age)
print("Students:", students)
print("Experience:", experience)

print("Height:", height)
print("Salary:", salary)

print("Name:", name)
print("City:", city)
print("Course:", course)

print("Likes Python:", likes_python)
print("Is Student:", is_student)

print("Skills:", skills)
print("Coordinates:", coordinates)
print("Unique Numbers:", unique_numbers)
print("Student:", student)


# -----------------------------
# 3. Identify Data Types
# -----------------------------

print("\n----- DATA TYPES -----")

print("age:", type(age))
print("students:", type(students))
print("experience:", type(experience))

print("height:", type(height))
print("salary:", type(salary))

print("name:", type(name))
print("city:", type(city))
print("course:", type(course))

print("likes_python:", type(likes_python))
print("is_student:", type(is_student))

print("skills:", type(skills))
print("coordinates:", type(coordinates))
print("unique_numbers:", type(unique_numbers))
print("student:", type(student))


# -----------------------------
# 4. Type Conversion
# -----------------------------

print("\n----- TYPE CONVERSION -----")


# String to Integer
value1 = int("100")

print("\nString to Integer")
print("Value:", value1)
print("Data Type:", type(value1))


# String to Float
value2 = float("45.67")

print("\nString to Float")
print("Value:", value2)
print("Data Type:", type(value2))


# Integer to String
value3 = str(500)

print("\nInteger to String")
print("Value:", value3)
print("Data Type:", type(value3))


# Integer to Boolean
value4 = bool(1)

print("\nInteger to Boolean")
print("Value:", value4)
print("Data Type:", type(value4))


# Tuple to List
value5 = list((1, 2, 3))

print("\nTuple to List")
print("Value:", value5)
print("Data Type:", type(value5))


# List to Tuple
value6 = tuple([1, 2, 3])

print("\nList to Tuple")
print("Value:", value6)
print("Data Type:", type(value6))


# List to Set
value7 = set([1, 2, 2, 3])

print("\nList to Set")
print("Value:", value7)
print("Data Type:", type(value7))


# -----------------------------
# 5. Additional Boolean Examples
# -----------------------------

print("\n----- BOOLEAN CONVERSION -----")

print("bool(1):", bool(1))
print("bool(0):", bool(0))

print("Type of bool(1):", type(bool(1)))
print("Type of bool(0):", type(bool(0)))


# -----------------------------
# 6. Conversion Summary
# -----------------------------

print("\n----- CONVERSION SUMMARY -----")

print('int("100"):', int("100"))
print('float("45.67"):', float("45.67"))
print("str(500):", str(500))
print("bool(1):", bool(1))
print("list((1, 2, 3)):", list((1, 2, 3)))
print("tuple([1, 2, 3]):", tuple([1, 2, 3]))
print("set([1, 2, 2, 3]):", set([1, 2, 2, 3]))