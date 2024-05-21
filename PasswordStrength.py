import re

def assess_password_strength(password):
    # Define criteria
    length_criteria = 8
    uppercase_criteria = True
    lowercase_criteria = True
    number_criteria = True
    special_char_criteria = True

    # Check length
    if len(password) < length_criteria:
        return "Password is too short. It should be at least {} characters long.".format(length_criteria)

    # Check for uppercase letters
    if uppercase_criteria and not any(char.isupper() for char in password):
        return "Password should contain at least one uppercase letter."

    # Check for lowercase letters
    if lowercase_criteria and not any(char.islower() for char in password):
        return "Password should contain at least one lowercase letter."

    # Check for numbers
    if number_criteria and not any(char.isdigit() for char in password):
        return "Password should contain at least one number."

    # Check for special characters
    if special_char_criteria and not re.search(r'[!@#$%^&*()\-_=+{};:,<.>/?]', password):
        return "Password should contain at least one special character."

    # If all criteria pass
    return "Password is strong!"

# Test the function
password = input("Enter your password: ")
print(assess_password_strength(password))
