import random
import string

# Function to get company policy from the user with error handling
def get_company_policy():
    policy = {}

    # Get and validate requirement for uppercase characters
    while True:
        try:
            policy['require_upper'] = int(input("\nAt least how many uppercase characters should your password contain? "))
            if policy['require_upper'] < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get and validate requirement for lowercase characters
    while True:
        try:
            policy['require_lower'] = int(input("At least how many lowercase characters should your password contain? "))
            if policy['require_lower'] < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get and validate requirement for digits
    while True:
        try:
            policy['require_digit'] = int(input("At least how many digits should your password contain? "))
            if policy['require_digit'] < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get and validate requirement for special characters
    while True:
        try:
            policy['require_special'] = int(input("At least how many special characters should your password contain? "))
            if policy['require_special'] < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    allowed_special_characters = "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~\""
    while True:
        policy['special_characters'] = input(f"Enter the special characters allowed. Leave blank for default special characters. (Default is {allowed_special_characters}): ")
        if not policy['special_characters']:
            policy['special_characters'] = allowed_special_characters
            break
        if all(char in allowed_special_characters for char in policy['special_characters']):
            break
        else:
            print(f"Invalid input. Only the following special characters are allowed: {allowed_special_characters}")

    # Get and validate minimum length
    while True:
        try:
            policy['min_length'] = int(input("Enter the minimum length for the password: "))
            total_required_chars = (policy['require_upper'] + policy['require_lower'] +
                                    policy['require_digit'] + policy['require_special'])
            if policy['min_length'] < total_required_chars or policy['min_length'] <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Minimum length must be at least the sum of all required character types and greater than zero.")

    # Get and validate maximum length
    while True:
        try:
            policy['max_length'] = int(input("Enter the maximum length for the password: "))
            if policy['max_length'] < policy['min_length']:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Maximum length must be greater than or equal to the minimum length.")

    # Display the policy details to the user
    print("\nPassword Policy Requirements:")
    print(f"- Minimum length: {policy['min_length']}")
    print(f"- Maximum length: {policy['max_length']}")
    print(f"- Requires at least {policy['require_upper']} uppercase characters")
    print(f"- Requires at least {policy['require_lower']} lowercase characters")
    print(f"- Requires at least {policy['require_digit']} digits")
    print(f"- Requires at least {policy['require_special']} special characters")
    print(f"- Allowed special characters: {policy['special_characters']}")

    return policy

# Function to check if the password length is sufficient
def check_length(password, min_length, max_length):
    return min_length <= len(password) <= max_length

# Function to check if the password contains the required number of uppercase and lowercase characters
def check_case(password, require_upper, require_lower):
    num_upper = sum(1 for char in password if char.isupper())
    num_lower = sum(1 for char in password if char.islower())
    return num_upper >= require_upper and num_lower >= require_lower

# Function to check if the password contains the required number of digits
def check_digit(password, require_digit):
    num_digits = sum(1 for char in password if char.isdigit())
    return num_digits >= require_digit

# Function to check if the password contains the required number of special characters
def check_special_character(password, require_special, special_characters):
    num_special = sum(1 for char in password if char in special_characters)
    return num_special >= require_special

# Function to generate a suggested password based on policy
def suggest_password(policy):
    password = []

    password.extend(random.choices(string.ascii_uppercase, k=policy['require_upper']))
    password.extend(random.choices(string.ascii_lowercase, k=policy['require_lower']))
    password.extend(random.choices(string.digits, k=policy['require_digit']))
    password.extend(random.choices(policy['special_characters'], k=policy['require_special']))

    remaining_length = policy['max_length'] - len(password)

    if remaining_length > 0:
        all_characters = string.ascii_letters + string.digits + policy['special_characters']
        password.extend(random.choices(all_characters, k=remaining_length))

    random.shuffle(password)
    return ''.join(password[:policy['max_length']])

# Main function to check the password strength based on company policy
def check_password_strength(password, policy):
    if not check_length(password, policy['min_length'], policy['max_length']):
        return f"Password must be between {policy['min_length']} and {policy['max_length']} characters long. Suggested password: {suggest_password(policy)}"
    if not check_case(password, policy['require_upper'], policy['require_lower']):
        return f"Password must contain at least {policy['require_upper']} uppercase and {policy['require_lower']} lowercase characters. Suggested password: {suggest_password(policy)}"
    if not check_digit(password, policy['require_digit']):
        return f"Password must contain at least {policy['require_digit']} digit(s). Suggested password: {suggest_password(policy)}"
    if not check_special_character(password, policy['require_special'], policy['special_characters']):
        return f"Password must contain at least {policy['require_special']} special character(s) from: {policy['special_characters']}. Suggested password: {suggest_password(policy)}"

    return "Your password meets the requirements!"

def main():
    company_policy = get_company_policy()

    while True:
        password = input("\nEnter your password: ")
        print(check_password_strength(password, company_policy))

        continue_choice = input("\nDo you want to test another password? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            break

# Example usage
if __name__ == "__main__":
    main()
