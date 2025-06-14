# Salary Tax Calculator
# This program calculates estimated tax based on Indian income tax slabs.

# Take user input for annual salary
salary = float(input("Enter your annual salary: "))

# Initialize tax to zero
tax = 0

# Calculate tax based on salary slabs
if salary <= 250000:
    tax = 0
elif salary <= 500000:
    # 5% tax on income above ₹2.5L
    tax = 0.05 * (salary - 250000)
elif salary <= 1000000:
    # 5% on ₹2.5L–5L + 10% on remaining up to ₹10L
    tax = 0.05 * 250000 + 0.10 * (salary - 500000)
else:
    # 5% on ₹2.5L–5L + 10% on ₹5L–10L + 20% on remaining above ₹10L
    tax = 0.05 * 250000 + 0.10 * 500000 + 0.20 * (salary - 1000000)

# Display the final tax amount
print("Estimated Tax you have to pay: ₹", tax)
