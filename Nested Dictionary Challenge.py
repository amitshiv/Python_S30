# ==========================================
# Python Nested Dictionaries
# ==========================================

# Create an employee dictionary.
# The "skills" key contains another dictionary,
# which makes this a nested dictionary.
employee = {
    "name": "Amit",
    "department": "Engineering",
    "skills": {
        "language": "Python",
        "database": "PostgreSQL",
        "cloud": "AWS"
    },
    "salary": 80000
}


# ==========================================
# 1. Print Employee Name
# ==========================================

print("Employee Name:", employee["name"])


# ==========================================
# 2. Print Department
# ==========================================

print("Department:", employee["department"])


# ==========================================
# 3. Print Complete Skills Dictionary
# ==========================================

print("Skills:", employee["skills"])


# ==========================================
# 4. Print Programming Language
# ==========================================

# First access the "skills" dictionary,
# then access the "language" key inside it.
print("Programming Language:", employee["skills"]["language"])


# ==========================================
# 5. Print Database
# ==========================================

print("Database:", employee["skills"]["database"])


# ==========================================
# 6. Print Cloud Technology
# ==========================================

print("Cloud Technology:", employee["skills"]["cloud"])


# ==========================================
# 7. Change Python to Python + JavaScript
# ==========================================

# Access the nested "language" key and update its value.
employee["skills"]["language"] = "Python + JavaScript"

print("Updated Language:", employee["skills"]["language"])


# ==========================================
# 8. Change Salary
# ==========================================

employee["salary"] = 90000

print("Updated Salary:", employee["salary"])


# ==========================================
# 9. Add Experience
# ==========================================

employee["experience"] = 3

print("Experience:", employee["experience"])


# ==========================================
# 10. Add Another Skill
# ==========================================

# Add a new key inside the nested "skills" dictionary.
employee["skills"]["framework"] = "Django"

print("Updated Skills:", employee["skills"])


# ==========================================
# 11. Print Final Employee Dictionary
# ==========================================

print("\nFinal Employee Details:")
print(employee)


# ==========================================
# Nested Dictionary Access
# ==========================================

# Main dictionary
#       ↓
# employee["skills"]
#
# Nested dictionary
#       ↓
# employee["skills"]["language"]
#
# In simple words:
#
# employee
#    └── skills
#         ├── language
#         ├── database
#         ├── cloud
#         └── framework
#
# To access a value inside a nested dictionary,
# move from the outer dictionary to the inner dictionary.