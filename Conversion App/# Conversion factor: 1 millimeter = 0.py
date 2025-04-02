# Conversion factors
def mm_to_inches(mm):
    return mm * 0.0393701

def feet_to_inches(feet):
    return feet * 12

def yards_to_inches(yards):
    return yards * 36

def meters_to_inches(meters):
    return meters * 39.3701

# Get unit selection from user
print("Select the unit of measurement:")
print("1. Millimeters")
print("2. Feet")
print("3. Yards")
print("4. Meters")

unit_choice = input("Enter your choice (1-4): ")

# Get the value from user
value = float(input("Enter the value: "))

# Convert based on selection
if unit_choice == "1":
    result = mm_to_inches(value)
    unit_name = "millimeters"
elif unit_choice == "2":
    result = feet_to_inches(value)
    unit_name = "feet"
elif unit_choice == "3":
    result = yards_to_inches(value)
    unit_name = "yards"
elif unit_choice == "4":
    result = meters_to_inches(value)
    unit_name = "meters"
else:
    print("Invalid choice!")
    exit()

# Output the result
print(f"{value} {unit_name} is equal to {result:.4f} inches.")
