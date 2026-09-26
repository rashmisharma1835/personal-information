# import string

# def validate_password(password: str) -> tuple[bool, list[str]]:
#     """
#     Validates a password against standard criteria.
#     Returns (True, []) if valid, or (False, [reasons]) if invalid.
#     """
#     errors = []

#     # 1. Check length
#     if len(password) < 8:
#         errors.append("Must be at least 8 characters long.")

#     # 2. Check uppercase
#     if not any(char in string.ascii_uppercase for char in password):
#         errors.append("Must contain at least one uppercase letter (A-Z).")

#     # 3. Check lowercase
#     if not any(char in string.ascii_lowercase for char in password):
#         errors.append("Must contain at least one lowercase letter (a-z).")

#     # 4. Check digits
#     if not any(char in string.digits for char in password):
#         errors.append("Must contain at least one digit (0-9).")

#     # 5. Check special characters
#     if not any(char in string.punctuation for char in password):
#         errors.append("Must contain at least one special character (!@#$%...).")

#     is_valid = len(errors) == 0
#     return is_valid, errors


# # --- Demonstration & Test Cases ---
# if __name__ == "__main__":
#     test_passwords = [
#         ("Secret1!", "Valid password meeting all criteria"),
#         ("short1!", "Invalid: Less than 8 characters"),
#         ("nouppercase123!", "Invalid: Missing uppercase character"),
#         ("NOLOWERCASE123!", "Invalid: Missing lowercase character"),
#         ("NoDigitsHere!", "Invalid: Missing numeric digit"),
#         ("NoSpecialChar123", "Invalid: Missing punctuation symbol"),
#     ]

#     print("=== Password Validator Output ===\n")
#     for pwd, label in test_passwords:
#         valid, feedback = validate_password(pwd)
#         status = "VALID" if valid else "INVALID"
#         print(f"Test case: {label}")
#         print(f"Status:    {status}")
#         if not valid:
#             for issue in feedback:
#                 print(f" - {issue}")
#         print("-" * 40)
import string

password = input("Enter your password: ")

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)

if len(password) < 8:
    print("Invalid Password: Minimum 8 characters required.")
elif not has_upper:
    print("Invalid Password: At least one uppercase character required.")
elif not has_lower:
    print("Invalid Password: At least one lowercase character required.")
elif not has_digit:
    print("Invalid Password: At least one number required.")
elif not has_special:
    print("Invalid Password: At least one special character required.")
else:
    print("Valid Password")