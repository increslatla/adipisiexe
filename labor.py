res = None  # Initialize the variable

# Some logic that may or may not assign a value to res
data = [1, 2, 3, 4, 5]
for num in data:
    if num > 3:
        res = num
        break

if res is not None:
    print(f"Found a number greater than 3: {res}")
else:
    print("No number greater than 3 found.")
