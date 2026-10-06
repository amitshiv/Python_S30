# ============================================================
# Python Loops - Realistic Data Processing & Problem Solving
# ============================================================


# ============================================================
# 1. Calculate Total Transaction Value Without sum()
# ============================================================

transactions = [1200, 450, 800, 1500, 2300, 700, 100]

total = 0

for transaction in transactions:
    total += transaction

print("Total transaction value:", total)


# ============================================================
# 2. Find Highest and Lowest Transaction
#    Without max() and min()
# ============================================================

highest = transactions[0]
lowest = transactions[0]

for transaction in transactions:
    if transaction > highest:
        highest = transaction

    if transaction < lowest:
        lowest = transaction

print("Highest transaction:", highest)
print("Lowest transaction:", lowest)


# ============================================================
# 3. Calculate Average Temperature
# ============================================================

temperatures = [32, 35, 28, 40, 38, 31, 42]

temperature_total = 0

for temperature in temperatures:
    temperature_total += temperature

average_temperature = temperature_total / len(temperatures)

print("\nAverage temperature:", average_temperature)


# ============================================================
# 4. Student Marks - Count Students in Different Ranges
# ============================================================

marks = [78, 92, 45, 67, 88, 53, 99]

count_90_plus = 0
count_75_89 = 0
count_50_74 = 0
count_below_50 = 0

for mark in marks:

    if mark >= 90:
        count_90_plus += 1

    elif mark >= 75:
        count_75_89 += 1

    elif mark >= 50:
        count_50_74 += 1

    else:
        count_below_50 += 1

print("\nStudent Marks Analysis:")
print("90+:", count_90_plus)
print("75-89:", count_75_89)
print("50-74:", count_50_74)
print("Below 50:", count_below_50)


# ============================================================
# 5. Simple Login System - Maximum 3 Attempts
# ============================================================

correct_password = "python123"

attempts = 0
login_successful = False

while attempts < 3:

    password = input("\nEnter password: ")

    if password == correct_password:
        print("Login successful!")
        login_successful = True
        break

    else:
        attempts += 1
        print("Incorrect password.")

        remaining_attempts = 3 - attempts

        if remaining_attempts > 0:
            print("Attempts remaining:", remaining_attempts)

if not login_successful:
    print("Account locked. Maximum attempts reached.")


# ============================================================
# 6. Products Costing More Than ₹2,000
# ============================================================

products = {
    "Laptop": 55000,
    "Phone": 30000,
    "Headphones": 2000,
    "Mouse": 700,
    "Keyboard": 1500
}

print("\nProducts costing more than ₹2,000:")

for product, price in products.items():

    if price > 2000:
        print(product, "₹", price)


# ============================================================
# 7. Accept 10 Numbers and Store Them in a List
# ============================================================

numbers = []

print("\nEnter 10 numbers:")

for i in range(10):

    number = int(input(f"Enter number {i + 1}: "))

    numbers.append(number)

print("Numbers entered:", numbers)


# ============================================================
# 8. Count Frequency of Every Character
#    Without using Counter
# ============================================================

text = "banana"

frequency = {}

for character in text:

    if character in frequency:
        frequency[character] += 1

    else:
        frequency[character] = 1

print("\nCharacter Frequency:")

for character, count in frequency.items():
    print(character, "->", count)


# ============================================================
# 9. Find Second-Largest Number Without sort()
# ============================================================

numbers = [10, 45, 23, 89, 67, 89, 34]

largest = None
second_largest = None

for number in numbers:

    if largest is None or number > largest:

        if number != largest:
            second_largest = largest

        largest = number

    elif number != largest and (
        second_largest is None or number > second_largest
    ):
        second_largest = number

print("\nLargest number:", largest)
print("Second-largest number:", second_largest)


# ============================================================
# 10. Check Whether a String is a Palindrome
#     Using Loops
# ============================================================

word = "madam"

reversed_word = ""

for character in word:
    reversed_word = character + reversed_word

if word == reversed_word:
    print("\n", word, "is a palindrome.")

else:
    print("\n", word, "is not a palindrome.")


# ============================================================
# 11. Number Pattern
# ============================================================

print("\nNumber Pattern:")

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end="")

    print()


# ============================================================
# 12. Basic ATM Simulation
# ============================================================

balance = 10000

while True:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Check balance
    if choice == "1":

        print("Current balance: ₹", balance)


    # Deposit money
    elif choice == "2":

        deposit = float(input("Enter deposit amount: "))

        if deposit > 0:
            balance += deposit
            print("Amount deposited successfully.")
            print("Updated balance: ₹", balance)

        else:
            print("Invalid deposit amount.")


    # Withdraw money
    elif choice == "3":

        withdrawal = float(input("Enter withdrawal amount: "))

        if withdrawal <= 0:
            print("Invalid withdrawal amount.")

        elif withdrawal > balance:
            print("Insufficient balance.")

        else:
            balance -= withdrawal
            print("Please collect your cash.")
            print("Updated balance: ₹", balance)


    # Exit ATM
    elif choice == "4":

        print("Thank you for using the ATM.")
        break


    # Invalid choice
    else:

        print("Invalid choice. Please select 1, 2, 3, or 4.")