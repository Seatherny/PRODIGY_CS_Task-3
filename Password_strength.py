import re

def assess_password_strength(password):
    feedback = []

    # Minimum length of 8 characters
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    
    # Should contain at least 2 uppercase letters
    if sum(1 for char in password if char.isupper()) < 2:
        feedback.append("Password should contain at least 2 uppercase letters.")
    
    # Should contain at least 4 digits
    if sum(1 for char in password if char.isdigit()) < 4:
        feedback.append("Password should contain at least 4 digits.")
    
    # Should contain at least one special character
    special_characters = "!@#$%^&*()-=_+[]{}|;:'\",.<>/?"
    if not any(char in special_characters for char in password):
        feedback.append(f"Password should contain at least one special character from: {special_characters}")
    
    # Should not contain spaces
    if ' ' in password:
        feedback.append("Password should not contain spaces.")
    
    if feedback:
        return False, feedback
    else:
        return True, ["Password is strong!"]

# Get password from the user
password = input("Enter your password: ")

# Check password strength
is_strong, messages = assess_password_strength(password)

# Provide feedback to the user
for message in messages:
    print(message)