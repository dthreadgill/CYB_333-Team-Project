# Function to get company policy from the user
def get_company_policy():
    """
    Get the company policy for password requirements from the user.

    Returns:
    dict: A dictionary containing the company's password policy.
    """
    policy = {}
    policy['min_length'] = int(input("Enter the minimum length for the password: "))
    policy['require_upper'] = input("Should the password contain uppercase characters? (yes/no): ").strip().lower() == 'yes'
    policy['require_lower'] = input("Should the password contain lowercase characters? (yes/no): ").strip().lower() == 'yes'
    policy['require_digit'] = input("Should the password contain digits? (yes/no): ").strip().lower() == 'yes'
    policy['require_special'] = input("Should the password contain special characters? (yes/no): ").strip().lower() == 'yes'
    return policy

# Function to check if the password length is sufficient
def check_length(password, min_length):
    """
    Check if the password is at least `min_length` characters long.

    Parameters:
    password (str): The password string to check.
    min_length (int): The minimum required length for the password.

    Returns:
    bool: True if the password length is at least `min_length`, False otherwise.
    """
    return len(password) >= min_length

# Function to check if the password contains both uppercase and lowercase characters
def check_case(password, require_upper, require_lower):
    """
    Check if the password contains required uppercase and lowercase characters.

    Parameters:
    password (str): The password string to check.
    require_upper (bool): Whether the password should contain uppercase characters.
    require_lower (bool): Whether the password should contain lowercase characters.

    Returns:
    bool: True if the password contains required uppercase and lowercase characters, False otherwise.
    """
    has_upper = any(char.isupper() for char in password) if require_upper else True
    has_lower = any(char.islower() for char in password) if require_lower else True
    return has_upper and has_lower

# Function to check if the password contains at least one digit
def check_digit(password, require_digit):
    """
    Check if the password contains at least one digit.

    Parameters:
    password (str): The password string to check.
    require_digit (bool): Whether the password should contain at least one digit.

    Returns:
    bool: True if the password contains at least one digit, False otherwise.
    """
    return any(char.isdigit() for char in password) if require_digit else True

# Function to check if the password contains at least one special character
def check_special_character(password, require_special):
    """
    Check if the password contains at least one special character.

    Parameters:
    password (str): The password string to check.
    require_special (bool): Whether the password should contain at least one special character.

    Returns:
    bool: True if the password contains at least one special character, False otherwise.
    """
    special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"
    return any(char in special_characters for char in password) if require_special else True

# Main function to check the password strength based on company policy
def check_password_strength(password, policy):
    """
    Check the overall strength of the password based on company policy.

    Parameters:
    password (str): The password string to check.
    policy (dict): The company's password policy.

    Returns:
    str: A message indicating the strength of the password.
    """
    if not check_length(password, policy['min_length']):
        return f"Password must be at least {policy['min_length']} characters long."
    if not check_case(password, policy['require_upper'], policy['require_lower']):
        return "Password must contain both uppercase and lowercase characters."
    if not check_digit(password, policy['require_digit']):
        return "Password must contain at least one digit."
    if not check_special_character(password, policy['require_special']):
        return "Password must contain at least one special character."

    return "Password is strong!"

# Example usage
company_policy = get_company_policy()
password = input("Enter your password: ")
print(check_password_strength(password, company_policy))
