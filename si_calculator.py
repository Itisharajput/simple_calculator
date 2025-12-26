#----------------SI CALCULATOR------
print("\n---Simple Intrest Calculator-------")
print("Formula: SI =( P * R * N) /100 ")

# Get inputs as strings first
principal_str = input("Enter Principal (P) :")
year_str = input("Enter Number of Years (N):")
rate_str = input("Enter Rate of interest (R):")

# Convert inputs to float for calculation
principal = float(princpal_str)
year = float(year_str)
rate = float(rate_str)

# Calculate Simple Intrest 
simple_intrest = (principal * year * rate) /100
# print the result
print(f"The Simple Interst (SI) is : {simple_intrest}")
