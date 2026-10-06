message = " Welcome To Python Programming Class "

# Remove extra spaces
print("Strip:", message.strip())

# Convert to lowercase
print("Lower:", message.lower())

# Convert to uppercase
print("Upper:", message.upper())

# Convert to title case
print("Title:", message.title())

# Replace Python with Advanced Python
print("Replace:", message.replace("Python", "Advanced Python"))

# Check starting text
print("Starts with Welcome:", message.strip().startswith("Welcome"))

# Check ending text
print("Ends with Class:", message.strip().endswith("Class"))

# Count occurrences of "o"
print("Count of o:", message.count("o"))

# Find position of Programming
print("Position of Programming:", message.find("Programming"))

# Split sentence into words
print("Words:", message.split())