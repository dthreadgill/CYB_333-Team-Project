# Function to check if the password length is sufficient
def check_length(password):
    """
    Check if the password is at least 8 characters long.
    
    Parameters:
    password (str): The password string to check.

    Returns:
    bool: True if the password length is at least 8, False otherwise.
    """
    return len(password) >= 8

# Function to check if the password contains both uppercase and lowercase characters
def check_case(password):
    """
    Check if the password contains both uppercase and lowercase characters.
    
    Parameters:
    password (str): The password string to check.

    Returns:
    bool: True if the password contains both uppercase and lowercase characters, False otherwise.
    """
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    return has_upper and has_lower

# Function to check if the password contains at least one digit
def check_digit(password):
    """
    Check if the password contains at least one digit.
    
    Parameters:
    password (str): The password string to check.

    Returns:
    bool: True if the password contains at least one digit, False otherwise.
    """
    return any(char.isdigit() for char in password)

# Function to check if the password contains at least one special character
def check_special_character(password):
    """
    Check if the password contains at least one special character.
    
    Parameters:
    password (str): The password string to check.

    Returns:
    bool: True if the password contains at least one special character, False otherwise.
    """
    special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"
    return any(char in special_characters for char in password)

# Main function to check the password strength
def check_password_strength(password):
    """
    Check the overall strength of the password based on various criteria.
    
    Parameters:
    password (str): The password string to check.

    Returns:
    str: A message indicating the strength of the password.
    """
    if not check_length(password):
        return "Password must be at least 8 characters long."
    if not check_case(password):
        return "Password must contain both uppercase and lowercase characters."
    if not check_digit(password):
        return "Password must contain at least one digit."
    if not check_special_character(password):
        return "Password must contain at least one special character."
    
    return "Password is strong!"

# Example usage
password = input("Enter your password: ")
print(check_password_strength(password))
