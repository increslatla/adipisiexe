import random

# Generate a random amount between 0.00000500 and 0.00000515, rounded to 8 decimal places
amount = round(random.uniform(0.00000500, 0.00000515), 8)

# Print the generated amount
print(amount)
