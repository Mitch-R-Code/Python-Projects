# Conversion factor: 1 millimeter = 0.0393701 inches
def mm_to_inches(mm):
    return mm * 0.0393701

# Input from the user
mm_input = float(input("Enter the value in millimeters: "))
inches = mm_to_inches(mm_input)

# Output the result
print(f"{mm_input} millimeters is equal to {inches:.4f} inches.")
int_inches = int(inches)
print(f"The integer part of the inches is {int_inches}")
decimal_inches = inches - int_inches
print(f"The decimal part of the inches is {decimal_inches}")

