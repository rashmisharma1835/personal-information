# Personal Information Program

print("--- Enter Your Personal Information ---")

# input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in feet): "))
email = input("Enter your email: ")
city = input("Enter your city: ")

# Formatted output display 
print("\n" + "="*30)
print("       USER PROFILE SUMMARY       ")
print("="*30)
print(f"Name   : {name}")
print(f"Age    : {age} years")
print(f"Height : {height} feet")
print(f"Email  : {email}")
print(f"City   : {city}")
print("="*30)